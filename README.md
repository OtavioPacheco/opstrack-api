## Configuração do ambiente de desenvolvimento

O projeto utiliza Flake8 para verificar o código Python e pre-commit
para executar essa verificação automaticamente antes dos commits.

### Pré-requisitos

- Git instalado.
- Python e pip instalados, na versão compatível com o projeto.

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd opstrack-api
```

Substitua `<URL_DO_REPOSITORIO>` pela URL do repositório da equipe.

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows, usando PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Windows, usando CMD:

```bat
.venv\Scripts\activate.bat
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

Instale as dependências de desenvolvimento:

```bash
python -m pip install -r requirements-dev.txt
```

Se o projeto possuir um arquivo `requirements.txt`, instale também
as dependências da aplicação:

```bash
python -m pip install -r requirements.txt
```

### 5. Instalar o hook

Com o ambiente virtual ativado, execute:

```bash
pre-commit install
```

Esse comando instala o hook na cópia local do repositório. Cada novo
integrante precisa executá-lo após clonar o projeto: versionar a
configuração não instala o hook automaticamente nas outras máquinas.

### 6. Verificar a configuração

Execute a verificação em todos os arquivos versionados:

```bash
pre-commit run --all-files
```

Se o resultado for `Passed`, a verificação passou. Caso apareçam erros,
corrija os arquivos indicados e execute o comando novamente.

### Uso no dia a dia

Mantenha o ambiente virtual ativado ao fazer commits. O Flake8 será
executado automaticamente sobre os arquivos Python incluídos no commit.

Se a verificação falhar, o commit será interrompido. Corrija os problemas,
adicione novamente os arquivos corrigidos com `git add` e tente fazer o
commit outra vez.

### Arquivos de configuração

- `.flake8`: define as regras de verificação do código.
- `.pre-commit-config.yaml`: configura a execução do Flake8 antes dos commits.
- `requirements-dev.txt`: lista as ferramentas de desenvolvimento.
