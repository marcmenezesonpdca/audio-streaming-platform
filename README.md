# Plataforma de Streaming de Áudio para Eventos

Uma plataforma web moderna para transmissão de áudio em alta qualidade para eventos, com sistema de acesso via PIN de 8 dígitos.

## 🎯 Visão Geral

Esta plataforma permite que organizadores de eventos criem experiências de áudio personalizadas para seus participantes. Cada evento possui um PIN único de 8 dígitos que os participantes usam para acessar o stream de áudio em alta qualidade.

## ✨ Funcionalidades Principais

### Para Organizadores (Painel Administrativo)
- ✅ Criação e gerenciamento de eventos
- ✅ Geração automática de PIN único de 8 dígitos
- ✅ Personalização visual (cores, logo, descrição)
- ✅ Configuração de URL de stream HLS
- ✅ Visualização e cópia do PIN do evento
- ✅ Gerenciamento de participantes registrados

### Para Participantes
- ✅ Acesso via PIN de 8 dígitos (formato XXXX-XXXX)
- ✅ Página de login simples e intuitiva
- ✅ Registro com nome e email
- ✅ Player de áudio HLS profissional
- ✅ Interface responsiva (otimizada para mobile)
- ✅ Personalização visual por evento

## 🛠️ Tecnologias Utilizadas

### Backend
- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados (desenvolvimento)
- **Flask-CORS** - Suporte a CORS

### Frontend
- **React** - Biblioteca JavaScript
- **Tailwind CSS** - Framework CSS
- **HLS.js** - Player de áudio HLS
- **Lucide React** - Ícones
- **Vite** - Build tool

## 📋 Pré-requisitos

- Python 3.8+
- Node.js 16+
- npm ou pnpm

## 🚀 Instalação e Configuração

### 1. Configuração do Backend

```bash
# Clone o repositório
git clone <seu-repositorio>
cd audio-streaming-platform

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor Flask
python src/main.py
```

O backend estará disponível em `http://localhost:5000`

### 2. Configuração do Frontend (Desenvolvimento)

```bash
# Navegue para o diretório do frontend
cd ../audio-streaming-frontend

# Instale as dependências
npm install
# ou
pnpm install

# Execute o servidor de desenvolvimento
npm run dev
# ou
pnpm dev
```

O frontend estará disponível em `http://localhost:5173`

### 3. Build para Produção

```bash
# No diretório do frontend
npm run build
# ou
pnpm build

# Copie os arquivos para o Flask
cp -r dist/* ../audio-streaming-platform/src/static/
```

## 📱 Como Usar

### Para Organizadores

1. **Acesse o painel administrativo**: `http://localhost:5000/admin`
2. **Crie um novo evento**: Clique em "Novo Evento"
3. **Preencha as informações**:
   - Nome do evento (obrigatório)
   - URL da logo (opcional)
   - Descrição (opcional)
   - URL do stream HLS (obrigatório para áudio)
   - Cores personalizadas (opcional)
4. **Obtenha o PIN**: Clique no botão "PIN" para visualizar e copiar
5. **Compartilhe o PIN**: Distribua o PIN de 8 dígitos para os participantes

### Para Participantes

1. **Acesse a página inicial**: `http://localhost:5000`
2. **Digite o PIN**: Insira o PIN de 8 dígitos no formato XXXX-XXXX
3. **Clique em "Acessar Evento"**
4. **Faça seu registro**: Preencha nome e email
5. **Aproveite o áudio**: Use fones de ouvido para melhor experiência

## 🔧 Configuração de Streaming

### Formatos Suportados
- **HLS (HTTP Live Streaming)** - Recomendado
- URLs devem terminar com `.m3u8`

### Exemplos de URLs de Stream
```
https://exemplo.com/stream/audio.m3u8
https://radio.exemplo.com/live.m3u8
```

### Configuração de Servidor de Streaming
Para configurar seu próprio servidor de streaming, consulte:
- **OBS Studio** com plugin HLS
- **FFmpeg** para conversão
- **Nginx** com módulo RTMP
- **Icecast** para streaming de rádio

## 🎨 Personalização Visual

Cada evento pode ser personalizado com:
- **Cor Primária**: Títulos e elementos principais
- **Cor Secundária**: Fundo e áreas secundárias  
- **Cor de Destaque**: Botões e elementos interativos
- **Logo**: Imagem personalizada do evento

## 📊 Estrutura do Banco de Dados

### Tabela: events
- `id` - ID único do evento
- `name` - Nome do evento
- `description` - Descrição (opcional)
- `logo_url` - URL da logo (opcional)
- `audio_stream_url` - URL do stream HLS
- `access_pin` - PIN de 8 dígitos único
- `primary_color` - Cor primária (hex)
- `secondary_color` - Cor secundária (hex)
- `accent_color` - Cor de destaque (hex)
- `created_at` - Data de criação

### Tabela: participants
- `id` - ID único do participante
- `event_id` - Referência ao evento
- `name` - Nome do participante
- `email` - Email do participante
- `registered_at` - Data de registro

## 🔌 API Endpoints

### Eventos
- `GET /api/events` - Listar todos os eventos
- `POST /api/events` - Criar novo evento
- `GET /api/events/{id}` - Obter evento específico
- `PUT /api/events/{id}` - Atualizar evento
- `DELETE /api/events/{id}` - Deletar evento
- `GET /api/events/{id}/pin` - Obter PIN do evento

### Acesso via PIN
- `POST /api/events/access` - Validar PIN e obter dados do evento
- `POST /api/events/pin/{pin}/register` - Registrar participante via PIN

### Participantes
- `GET /api/events/{id}/participants` - Listar participantes do evento

## 🚀 Deploy em Produção

### Opções de Hospedagem Gratuita
1. **Render.com** (Recomendado)
2. **Railway.app**
3. **Heroku** (com limitações)

### Configuração para Deploy
1. Configure as variáveis de ambiente
2. Use PostgreSQL para produção
3. Configure CORS adequadamente
4. Use HTTPS para streams seguros

## 🔒 Segurança

- PINs são únicos e gerados automaticamente
- Validação de entrada em todos os formulários
- CORS configurado adequadamente
- Sanitização de dados de entrada

## 🐛 Solução de Problemas

### Problemas Comuns

**Erro: "PIN inválido"**
- Verifique se o PIN foi digitado corretamente
- Certifique-se de que o evento ainda existe

**Áudio não reproduz**
- Verifique se a URL do stream está correta
- Teste a URL diretamente no navegador
- Certifique-se de que o formato é HLS (.m3u8)

**Interface não carrega**
- Verifique se o build do frontend foi copiado para `/src/static/`
- Certifique-se de que o Flask está servindo arquivos estáticos

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor:
1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

## 📞 Suporte

Para suporte e dúvidas:
- Abra uma issue no GitHub
- Consulte a documentação
- Verifique os logs do servidor para debugging

---

**Desenvolvido com ❤️ para eventos de áudio de alta qualidade**

