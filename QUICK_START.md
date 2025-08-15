# 🚀 Guia de Início Rápido - Sistema de PIN

**Para usuários leigos - 30 minutos para colocar sua plataforma no ar!**

## 📋 O que você vai conseguir fazer

Ao final deste guia, você terá:
- ✅ Uma plataforma de streaming de áudio funcionando na internet
- ✅ Sistema de acesso via PIN de 8 dígitos
- ✅ Painel para gerenciar seus eventos
- ✅ Interface mobile para participantes

## 🎯 Passo 1: Preparar o Código

### 1.1 Fazer Upload para o GitHub

1. **Acesse o GitHub** e faça login na sua conta
2. **Crie um novo repositório:**
   - Clique no `+` no canto superior direito
   - Selecione "New repository"
   - Nome: `audio-streaming-platform`
   - Deixe como "Public"
   - **NÃO marque** nenhuma opção adicional
   - Clique em "Create repository"

3. **No seu computador:**
   - **Baixe o arquivo ZIP** que te enviei (`audio-streaming-platform-pin-final.zip`).
   - **Descompacte** o arquivo em uma pasta no seu computador (ex: `C:\Projetos\audio-streaming-platform`).
   - **Abra o terminal/prompt de comando** e navegue até essa pasta:
     ```bash
     cd caminho/para/audio-streaming-platform
     ```
   - **Inicialize o Git e faça o primeiro push:**
     ```bash
     git init
     git add .
     git commit -m "Initial commit of audio streaming platform"
     git remote add origin https://github.com/SEU_USUARIO/audio-streaming-platform.git
     git branch -M main
     git push -u origin main
     ```

## 🌐 Passo 2: Implantar no Render.com (GRATUITO)

### 2.1 Criar Conta no Render

1. **Acesse:** https://render.com
2. **Clique em "Get Started"**
3. **Conecte com GitHub** (mais fácil)
4. **Autorize o Render** a acessar seus repositórios

### 2.2 Criar o Serviço Web

1. **No painel do Render, clique em "New +"**
2. **Selecione "Web Service"**
3. **Conecte seu repositório:**
   - Procure por `audio-streaming-platform`
   - Clique em "Connect"

### 2.3 Configurar o Deploy

**Configurações importantes:**
- **Name:** `audio-streaming-platform` (ou qualquer nome)
- **Region:** `Oregon (US West)` (mais próximo)
- **Branch:** `main`
- **Root Directory:** deixe vazio ou coloque `.`
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python src/main.py`

### 2.4 Configurar Variáveis de Ambiente

Na seção "Environment Variables", adicione:
- **Key:** `FLASK_ENV` **Value:** `production`
- **Key:** `PORT` **Value:** `5000`

### 2.5 Finalizar Deploy

1. **Clique em "Create Web Service"**
2. **Aguarde 5-10 minutos** (o Render vai construir sua aplicação)
3. **Quando aparecer "Live"**, sua plataforma está no ar! 🎉

## 🎉 Passo 3: Testar sua Plataforma

### 3.1 Acessar o Painel Administrativo

1. **Copie a URL** que o Render forneceu (algo como `https://seu-app.onrender.com`)
2. **Adicione `/admin`** no final: `https://seu-app.onrender.com/admin`
3. **Você verá o painel administrativo!**

### 3.2 Criar seu Primeiro Evento

1. **Clique em "Novo Evento"**
2. **Preencha:**
   - Nome: "Meu Primeiro Evento"
   - Descrição: "Teste da plataforma"
   - URL do Stream: deixe vazio por enquanto
3. **Clique em "Criar Evento"**

### 3.3 Obter o PIN

1. **Clique no botão "PIN"** do evento criado
2. **Anote o PIN de 8 dígitos** (ex: 12345678)
3. **Clique em "Copiar PIN"** para facilitar

### 3.4 Testar como Participante

1. **Acesse a URL principal** (sem `/admin`)
2. **Digite o PIN** no formato XXXX-XXXX
3. **Clique em "Acessar Evento"**
4. **Preencha nome e email**
5. **Clique em "Acessar Áudio"**
6. **Sucesso!** Você verá a tela do player

## 🎵 Passo 4: Configurar Streaming de Áudio (Opcional)

### Para usar áudio real, você precisa de uma URL HLS (.m3u8)

**Opções gratuitas para teste:**
1. **Rádios online:** Muitas têm streams HLS públicos
2. **OBS Studio:** Configure para gerar stream HLS
3. **Icecast:** Servidor de streaming gratuito

**Como adicionar:**
1. No painel admin, clique em "Editar" no seu evento
2. Cole a URL HLS no campo "URL do Stream de Áudio"
3. Salve as alterações

## 📱 Passo 5: Usar no Dia do Evento

### Para Organizadores:
1. **Acesse:** `https://seu-app.onrender.com/admin`
2. **Clique em "PIN"** para ver o PIN do evento
3. **Compartilhe o PIN** com os participantes
4. **Diga para acessarem:** `https://seu-app.onrender.com`

### Para Participantes:
1. **Acessem:** `https://seu-app.onrender.com`
2. **Digitem o PIN** que você forneceu
3. **Façam o registro** com nome e email
4. **Usem fones de ouvido** para melhor experiência

## 🔧 Solução de Problemas Rápidos

### ❌ "Application failed to respond"
- **Aguarde 2-3 minutos** (o Render pode estar "acordando" o serviço)
- **Verifique os logs** no painel do Render

### ❌ "PIN inválido"
- **Verifique se digitou corretamente** (8 dígitos)
- **Certifique-se** de que o evento existe no painel admin

### ❌ "Áudio não funciona"
- **Normal se não configurou URL de stream**
- **Teste com uma rádio online** que tenha stream HLS

### ❌ "Página não carrega"
- **Verifique a URL** (deve ser a fornecida pelo Render)
- **Tente em modo anônimo** do navegador

## 💡 Dicas para o Sucesso

### Antes do Evento:
- ✅ **Teste tudo** com antecedência
- ✅ **Compartilhe o PIN** apenas no dia do evento
- ✅ **Tenha um backup** do PIN anotado

### Durante o Evento:
- ✅ **Monitore o painel admin** para ver participantes
- ✅ **Tenha a URL principal** sempre à mão
- ✅ **Oriente sobre fones de ouvido**

### Após o Evento:
- ✅ **Exporte a lista** de participantes se necessário
- ✅ **Mantenha o evento** para referência futura

## 🎊 Parabéns!

Sua plataforma de streaming de áudio está funcionando! 

**URL do seu painel:** `https://seu-app.onrender.com/admin`
**URL para participantes:** `https://seu-app.onrender.com`

---

**💬 Precisa de ajuda?** 
- Verifique os logs no painel do Render
- Teste em diferentes navegadores
- Certifique-se de que a internet está estável

