# 📅 Plano de Trabalho – PlantAgora (3 meses)

## 👥 Equipe

* **Backend**: 1 Oreia seca
* **Mobile**: 2 Oreias secas
* **QA/Testes**: 1 Doidão

---

## 🗂 Organização em Sprints

### Sprint 1 (Semanas 1–2) – Fundamentos e Setup

* **Backend**

  * [ ] Revisar autenticação JWT → confirmar se **refresh token** está implementado.
  * [ ] Documentar endpoints existentes via **drf-spectacular** (Swagger/ReDoc) - No momento usamos MkDocs.
  * [ ] Adicionar validações básicas nos serializers (email válido, CPF, CEP, etc.).

* **Mobile**

  * [ ] Reorganizar estrutura de pastas (`src/`, `components/ui`, `screens`, `services`).
  * [ ] Configurar **ESLint + Prettier + Husky** (lint + format on commit).
  * [ ] Revisar telas de login/registro.
  * [ ] Revisar demais telas e verificar quais precisam conectar com backend real (remover mocks).

* **QA**

  * [ ] Levantar **casos de teste manuais** (login, registro, CRUD hortas).
  * [ ] Testar Features Backend & Frontend.

* **Todos**
  * [ ] Configurar ambiente de testes automatizados (pytest no backend, Jest no mobile) - Verificar se os testadores atuais estão funcionando.

* **Critério de aceite**:

  * Backend: Doc Swagger acessível
  * Mobile: build Expo rodando sem mocks
  * QA: checklist de testes manuais publicado no repositório
  
  * Todos: Aplicação sem mocks

---

### Sprint 2 (Semanas 3–4) – Qualidade e Cobertura

* **Backend**
  * [ ] Criar testes unitários para models principais (Grower, Garden, GardenBed).
  * [ ] Adicionar **rate limiting** (django-ratelimit).

* **Mobile**
  * [ ] Implementar **Context API** para autenticação global.
  * [ ] Ativar **strict mode** no TypeScript (`tsconfig.json`).
  * [ ] Criar componentes reutilizáveis: `Button`, `Input`, `Card`.

* **QA**
  * [ ] Implementar testes de API básicos (pytest + DRF APITestCase).
  * [ ] Configurar pipeline para rodar testes no PR (integração com GitHub Actions) - Verificar se a existente já atende a este requisito.

* **Critério de aceite**:
  * Cobertura de testes backend ≥ 30%
  * Login persistente funcionando (token guardado em storage)
  * CI rodando testes em todos os PRs

---

### Sprint 3 (Semanas 5–6) – Segurança e UX

* **Backend**
  * [ ] Configurar headers de segurança (`SECURE_HSTS_SECONDS`, CSP, etc.).
  * [ ] Adicionar sanitização de inputs (evitar HTML malicioso).

* **Mobile**
  * [ ] Usar **expo-secure-store** para armazenar tokens.
  * [ ] Criar tela inicial com resumo da horta (dados reais via API).
  * [ ] Implementar **loading/error states** nos componentes.

* **QA**
  * [ ] Criar testes de integração: fluxo login → criar horta → listar hortas.
  * [ ] Documentar bugs encontrados e abrir issues.

* **Critério de aceite**:
  * Tokens salvos em `SecureStore` (não em AsyncStorage puro)
  * Backend com headers de segurança ativos
  * Testes de integração cobrindo pelo menos 1 fluxo completo

---

### Sprint 4 (Semanas 7–8) – Features e Design System

* **Backend**
  * [ ] Revisar queries pesadas e aplicar `.select_related()` / `.prefetch_related()`.
  * [ ] Criar endpoint para estatísticas simples (ex.: nº de hortas ativas).

* **Mobile**
  * [ ] Implementar tela de listagem de hortas (usando FlatList).
  * [ ] Implementar cache com **React Query** para dados da API.

* **QA**
  * [ ] Criar testes automatizados para UI do mobile (React Native Testing Library).
  * [ ] Medir cobertura de testes (backend + mobile).

* **Critério de aceite**:
  * Tela de hortas consumindo dados reais com cache
  * Estatísticas acessíveis por endpoint novo
  * Cobertura total de testes ≥ 50%

---

### Sprint 5 (Semanas 9–10) – Integração e Performance

* **Backend**
  * [ ] Implementar cache Redis em endpoint de estatísticas.
  * [ ] Monitoramento básico (health check, logs estruturados).

* **Mobile**
  * [ ] Otimizar imagens (usar `expo-image` com cache).
  * [ ] Lazy loading em telas pesadas do `expo-router`.
  * [ ] Preparar **build Android** com EAS Build.

* **QA**
  * [ ] Testes de performance básicos (tempo de resposta API).
  * [ ] Configurar **Sentry** no backend e mobile.

* **Critério de aceite**:
  * Build Android gerado e testado em device
  * Redis funcionando no backend
  * Sentry reportando erros reais

---

### Sprint 6 (Semanas 11–12) – Entrega Final e Consolidação

* **Backend**
  * [ ] Documentar ADRs (decisões arquiteturais).
  * [ ] Revisar segurança antes do deploy final.

* **Mobile**
  * [ ] Criar tela de perfil do usuário (dados reais via API).
  * [ ] Dark mode básico.

* **QA**
  * [ ] Checklist final de regressão.
  * [ ] Relatório de bugs e métricas de testes.

* **Critério de aceite**:
  * App pronto para publicação na Play Store
  * Documentação atualizada (backend + mobile)
  * QA entrega relatório final de qualidade

---

## 📊 Metas do Programa
* **Cobertura de testes**: ≥ 60% (backend + mobile)
* **Bugs críticos**: 0 no release final
* **Tempo de setup**: < 30min para novos devs
* **App**: login, registro, listagem de hortas, perfil funcionando com backend real

---

## 🔗 Recursos

* [Django Best Practices](https://django-best-practices.readthedocs.io/)
* [DRF Spectacular](https://drf-spectacular.readthedocs.io/)
* [React Query](https://tanstack.com/query/latest)
* [React Native Testing Library](https://testing-library.com/docs/react-native-testing-library/intro/)
* [Expo Secure Store](https://docs.expo.dev/versions/latest/sdk/securestore/)
* [Sentry](https://sentry.io/welcome/)