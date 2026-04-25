#!/usr/bin/env bats

setup() {
  # Create a temporary directory to hold our mocked commands
  export MOCK_DIR="$(mktemp -d)"
  export PATH="${MOCK_DIR}:${PATH}"
  export SCRIPT_PATH="$(dirname "$BATS_TEST_FILENAME")/../install.sh"
  export WORK_DIR="$(mktemp -d)"

  # Crear un .env.example falso para las pruebas de entorno
  touch "${WORK_DIR}/.env.example"
}

teardown() {
  # Clean up mocked executables
  rm -rf "${MOCK_DIR}"
  rm -rf "${WORK_DIR}"
}

@test "install.sh fails when docker is missing" {
  # No creamos el mock de docker, por lo que 'command -v docker' fallará
  run bash "$SCRIPT_PATH"
  [ "$status" -eq 1 ]
  [[ "$output" == *"Docker is required but not installed."* ]]
}

@test "install.sh fails when docker compose is missing" {
  # Mock docker command to fail specifically when 'compose version' is called
  cat << 'EOF' > "${MOCK_DIR}/docker"
#!/bin/bash
if [ "$1" == "compose" ] && [ "$2" == "version" ]; then
  exit 1
fi
exit 0
EOF
  chmod +x "${MOCK_DIR}/docker"

  run bash "$SCRIPT_PATH"
  [ "$status" -eq 1 ]
  [[ "$output" == *"Docker Compose is required but not installed."* ]]
}

@test "install.sh creates .env from template if missing and exits" {
  # Mock docker command to succeed
  cat << 'EOF' > "${MOCK_DIR}/docker"
#!/bin/bash
exit 0
EOF
  chmod +x "${MOCK_DIR}/docker"

  cd "${WORK_DIR}"
  run bash "$SCRIPT_PATH"

  [ "$status" -eq 0 ]
  [[ "$output" == *"Creating .env from template..."* ]]
  [ -f ".env" ]
}

@test "install.sh proceeds when docker compose is installed and .env exists" {
  # Mock docker command to always succeed
  cat << 'EOF' > "${MOCK_DIR}/docker"
#!/bin/bash
exit 0
EOF
  chmod +x "${MOCK_DIR}/docker"

  cd "${WORK_DIR}"
  touch .env # Simulamos que el usuario ya configuró su entorno

  run bash "$SCRIPT_PATH"
  # Solo debe mostrar los mensajes de build (que fallarían en el mock, pero probamos el flujo)
  [[ "$output" == *"Building containers..."* ]]
}
