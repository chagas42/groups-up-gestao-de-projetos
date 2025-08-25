# StudyConnect - Requisitos Funcionais e User Stories

## Identificação dos Atores

### 1. **Visitante (Não Autenticado)**
Usuário que acessa a plataforma sem estar logado

### 2. **Estudante Registrado**
Usuário autenticado que pode participar de grupos

### 3. **Criador de Grupo**
Estudante que criou um ou mais grupos (herda todas as permissões de Estudante)

### 4. **Administrador**
Responsável pela moderação da plataforma e gerenciamento de categorias

---

## Requisitos Funcionais por Ator

### **VISITANTE (Não Autenticado)**

#### RF01 - Visualizar Landing Page
- **Descrição:** Exibir informações sobre a plataforma, benefícios e call-to-action
- **Critérios:** Interface atrativa com exemplos de grupos e depoimentos

#### RF02 - Buscar Grupos Públicos
- **Descrição:** Visualizar lista de grupos públicos sem poder interagir
- **Critérios:** Mostrar apenas informações básicas (título, descrição, categoria)

#### RF03 - Realizar Cadastro
- **Descrição:** Criar nova conta fornecendo dados básicos
- **Critérios:** Validação de email único, senha forte, campos obrigatórios

#### RF04 - Realizar Login
- **Descrição:** Autenticar-se na plataforma
- **Critérios:** Validação de credenciais, redirecionamento para dashboard

---

### **ESTUDANTE REGISTRADO**

#### RF05 - Visualizar Dashboard Pessoal
- **Descrição:** Acessar painel com visão geral da atividade
- **Critérios:** Mostrar grupos ativos, solicitações pendentes, sugestões

#### RF06 - Gerenciar Perfil
- **Descrição:** Editar informações pessoais e interesses
- **Critérios:** Atualizar nome, curso, áreas de interesse, foto (opcional)

#### RF07 - Buscar e Filtrar Grupos
- **Descrição:** Encontrar grupos por categoria, tags, modalidade
- **Critérios:** Filtros funcionais, paginação, busca por palavra-chave

#### RF08 - Solicitar Participação em Grupo
- **Descrição:** Enviar pedido para entrar em grupos privados/aprovação
- **Critérios:** Para grupos públicos: entrada automática; privados: solicitar aprovação

#### RF09 - Sair de Grupo
- **Descrição:** Remover-se de grupos que participa
- **Critérios:** Confirmação obrigatória, atualização automática das listas

#### RF10 - Visualizar Detalhes do Grupo
- **Descrição:** Ver informações completas de grupos que participa
- **Critérios:** Membros, detalhes de contato, informações de encontro

#### RF11 - Gerenciar Notificações
- **Descrição:** Visualizar e marcar notificações como lidas
- **Critérios:** Lista de notificações por data, contadores de não lidas

---

### **CRIADOR DE GRUPO**

#### RF12 - Criar Novo Grupo
- **Descrição:** Estabelecer novo grupo de estudos
- **Critérios:** Título único, descrição clara, categoria obrigatória, configurações de privacidade

#### RF13 - Editar Informações do Grupo
- **Descrição:** Modificar dados do grupo criado
- **Critérios:** Apenas criador pode editar, histórico de alterações

#### RF14 - Gerenciar Membros
- **Descrição:** Aprovar/rejeitar solicitações e remover membros
- **Critérios:** Notificações automáticas, limite máximo de participantes

#### RF15 - Alterar Status do Grupo
- **Descrição:** Pausar, reativar ou finalizar grupo
- **Critérios:** Estados: Ativo, Pausado, Finalizado; notificar membros sobre mudanças

#### RF16 - Excluir Grupo
- **Descrição:** Remover grupo da plataforma
- **Critérios:** Confirmação dupla, notificar todos os membros, exclusão permanente

#### RF17 - Transferir Propriedade
- **Descrição:** Passar liderança do grupo para outro membro
- **Critérios:** Apenas para membros ativos, confirmação de ambas as partes

---

### **ADMINISTRADOR**

#### RF18 - Gerenciar Categorias
- **Descrição:** Criar, editar e remover categorias de grupos
- **Critérios:** Categorias únicas, impossível excluir se houver grupos vinculados

#### RF19 - Moderar Conteúdo
- **Descrição:** Revisar e remover conteúdo inapropriado
- **Critérios:** Poder de editar/excluir qualquer grupo, notificar usuários sobre ações

#### RF20 - Visualizar Relatórios
- **Descrição:** Acessar métricas da plataforma
- **Critérios:** Número de usuários, grupos ativos, categorias mais populares

---

## User Stories Detalhadas

### **VISITANTE**

**US01 - Descobrir a Plataforma**
```
Como visitante
Quero ver uma landing page atrativa
Para entender o valor da plataforma e me cadastrar

Critérios de Aceitação:
- Visualizo exemplos de grupos de estudo
- Vejo depoimentos de usuários
- Tenho acesso fácil aos botões de cadastro/login
- Posso navegar por grupos públicos sem me cadastrar
```

**US02 - Explorar Grupos Sem Compromisso**
```
Como visitante
Quero ver grupos disponíveis
Para avaliar se vale a pena me cadastrar

Critérios de Aceitação:
- Vejo lista de grupos públicos
- Posso filtrar por categoria
- Vejo informações básicas (não contatos)
- Sou direcionado para cadastro ao tentar interagir
```

### **ESTUDANTE REGISTRADO**

**US03 - Encontrar Grupo de Estudo**
```
Como estudante registrado
Quero buscar grupos da minha área
Para encontrar pessoas com interesses similares

Critérios de Aceitação:
- Posso filtrar por categoria (Exatas, Humanas, etc.)
- Posso buscar por palavras-chave
- Vejo se o grupo tem vagas disponíveis
- Posso ver modalidade (presencial/online/híbrido)
```

**US04 - Participar de Grupo**
```
Como estudante registrado
Quero entrar em um grupo de interesse
Para participar dos estudos colaborativos

Critérios de Aceitação:
- Em grupos públicos, entro automaticamente
- Em grupos privados, envio solicitação
- Recebo notificação sobre aprovação/rejeição
- Vejo o grupo na minha lista após aprovação
```

**US05 - Gerenciar Minhas Participações**
```
Como estudante registrado
Quero ver todos meus grupos
Para acompanhar minhas atividades de estudo

Critérios de Aceitação:
- Vejo lista de grupos ativos que participo
- Posso acessar detalhes de cada grupo
- Posso sair de grupos quando necessário
- Recebo confirmação antes de sair
```

### **CRIADOR DE GRUPO**

**US06 - Criar Grupo de Estudo**
```
Como criador de grupo
Quero formar um novo grupo
Para organizar estudos na minha área de interesse

Critérios de Aceitação:
- Defino título e descrição clara
- Escolho categoria apropriada
- Configuro se é público, privado ou por aprovação
- Estabeleço número máximo de participantes
- Defino modalidade (presencial/online/híbrido)
```

**US07 - Gerenciar Solicitações**
```
Como criador de grupo
Quero aprovar membros do meu grupo
Para manter qualidade e foco dos estudos

Critérios de Aceitação:
- Vejo lista de solicitações pendentes
- Posso ver perfil dos solicitantes
- Aprovo ou rejeito com um clique
- Solicitante recebe notificação automática
```

**US08 - Atualizar Informações do Grupo**
```
Como criador de grupo
Quero editar detalhes do meu grupo
Para manter informações sempre atualizadas

Critérios de Aceitação:
- Posso modificar horários de encontro
- Posso atualizar local de reunião
- Posso alterar descrição conforme evolução
- Membros são notificados sobre mudanças importantes
```

**US09 - Pausar Grupo Temporariamente**
```
Como criador de grupo
Quero pausar o grupo durante férias
Para retomar depois sem perder os membros

Critérios de Aceitação:
- Grupo fica marcado como "Pausado"
- Membros são notificados sobre pausa
- Grupo não aparece em buscas públicas
- Posso reativar quando necessário
```

### **ADMINISTRADOR**

**US10 - Organizar Categorias**
```
Como administrador
Quero gerenciar categorias da plataforma
Para manter organização e facilitar buscas

Critérios de Aceitação:
- Posso criar novas categorias
- Posso editar nomes de categorias existentes
- Não posso excluir categorias com grupos ativos
- Mudanças aparecem imediatamente na plataforma
```

**US11 - Moderar Conteúdo Inadequado**
```
Como administrador
Quero remover conteúdo inapropriado
Para manter ambiente seguro e educativo

Critérios de Aceitação:
- Posso editar/excluir qualquer grupo
- Posso suspender usuários problemáticos
- Envio notificação explicando ação tomada
- Mantenho log das ações de moderação
```

---

## Fluxos Principais

### **Fluxo 1: Novo Usuário Encontra Grupo**
1. Visitante acessa landing page
2. Explora grupos públicos
3. Realiza cadastro
4. Busca grupos de interesse
5. Solicita participação
6. Aguarda aprovação (se necessário)
7. Participa do grupo

### **Fluxo 2: Criação e Gestão de Grupo**
1. Estudante decide criar grupo
2. Preenche informações do grupo
3. Define configurações de privacidade
4. Publica grupo
5. Gerencia solicitações de entrada
6. Atualiza informações conforme necessário
7. Modera participações

### **Fluxo 3: Descoberta e Participação**
1. Estudante faz login
2. Acessa dashboard personalizado
3. Vê sugestões baseadas no perfil
4. Filtra grupos por categoria/tags
5. Escolhe grupo de interesse
6. Ingressa ou solicita aprovação
7. Acessa detalhes e informações de contato