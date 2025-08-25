# Groups Up - Gestão de Projetos

Monorepo com frontend Next.js e backend Flask Python.

## Estrutura do Projeto

```
apps/
  ├── frontend/          # Aplicação Next.js
  └── backend/           # API Flask Python
```

## Comandos

### Desenvolvimento

```bash
# Instalar dependências
npm install

# Frontend (Next.js)
npm run start:frontend
# ou
nx serve frontend

# Backend (Flask)
npm run start:backend  
# ou
nx serve backend
```

### Setup do Backend

1. Criar ambiente virtual Python:
```bash
cd apps/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Instalar dependências:
```bash
nx install backend
# ou
cd apps/backend && pip install -r requirements.txt
```

3. Configurar variáveis de ambiente:
```bash
cd apps/backend
cp .env.example .env
```

## URLs de Desenvolvimento

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **Backend Health Check**: http://localhost:5000/api/health