# Contributing to AI-Based Cyber Fraud Alert System

Thank you for contributing! Please follow these guidelines to ensure smooth collaboration.

---

## 🔀 Branching Strategy (GitFlow)

We use the **GitFlow branching model**:

- `main` → Production-ready code (stable releases only).
- `develop` → Integration branch (all features go here first).
- `feature/<name>` → New features (e.g. `feature/fraud-detection-api`).
- `bugfix/<name>` → Fixes for bugs found in development.
- `hotfix/<name>` → Urgent fixes directly to production.
- `release/<version>` → Release preparation (e.g. `release/v1.0.0`).

### Examples
```
feature/ml-model-training
feature/dashboard-ui
bugfix/api-timeout-issue
hotfix/security-vulnerability
```

---

## 📦 Development Workflow

1. **Start from `develop`**
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/my-feature
   git push -u origin feature/my-feature
   ```

3. **Work locally** (commit often, push regularly)
   ```bash
   git add .
   git commit -m "feat(api): add fraud detection endpoint"
   git push origin feature/my-feature
   ```

4. **Sync with latest `develop`** to avoid conflicts
   ```bash
   git checkout develop
   git pull origin develop
   git checkout feature/my-feature
   git merge develop
   ```

5. **Open a Pull Request (PR)**
   - Source branch → `develop`
   - Fill PR template
   - Request reviewers
   - Wait for approval before merging

6. **Merge**  
   - Requires **1 approval** for `develop`  
   - Requires **2 approvals** for `main`

---

## 📝 Commit Message Guidelines

Follow **Conventional Commits** format:

```
<type>(<scope>): <subject>
```

### Types
- `feat` → New feature
- `fix` → Bug fix
- `docs` → Documentation changes
- `style` → Formatting (no logic change)
- `refactor` → Code restructuring
- `test` → Adding/updating tests
- `chore` → Maintenance tasks
- `security` → Security-related changes

### Scopes
- `api` → Backend API
- `ui` → Frontend UI
- `ml` → Machine learning model
- `db` → Database
- `ci` → CI/CD pipeline

### Examples
✅ Good:
```
feat(api): add fraud detection endpoint
fix(ui): resolve dashboard loading issue
chore(ci): update GitHub Actions pipeline
```

❌ Bad:
```
updated stuff
fix bug
changes
```

---

## ✅ Code Review Checklist

Before approving a PR, check:
- [ ] Code builds without errors
- [ ] Tests pass (backend: `pytest`, frontend: `npm test`)
- [ ] No hardcoded secrets (API keys, passwords)
- [ ] Follows project style guidelines
- [ ] Documentation updated if needed

---

## 🔒 Security Guidelines

- Never commit credentials, secrets, or API keys
- Use environment variables (`.env`) instead
- Security-sensitive changes require explicit review from **Nishchay**

---

## 👥 Communication

- **Daily standups (recommended)** → Share progress and blockers
- **Weekly sync** → Review project timeline and plan features
- **Emergency**:
  - Critical bugs: Tag @everyone in team chat
  - Security issues: Message @Nishchay + @Dileep
  - Deployment issues: Message @Rahul (DevOps)

---

Happy contributing! 🚀
