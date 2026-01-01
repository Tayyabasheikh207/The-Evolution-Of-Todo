<!--
Sync Impact Report:
Version Change: Template → 1.0.0
Modified Principles: All placeholder principles replaced with concrete Evolution of Todo principles
Added Sections:
  - Spec-Driven Development Mandate
  - Agent Behavior Rules
  - Phase Governance
  - Technology Stack Constraints
  - Quality & Architecture Standards
  - Development Workflow
Removed Sections: All placeholder sections replaced with concrete sections
Templates Requiring Updates:
  ✅ .specify/templates/plan-template.md - Constitution Check section aligned with new principles
  ✅ .specify/templates/spec-template.md - Functional requirements align with SDD mandate
  ✅ .specify/templates/tasks-template.md - Task categorization reflects quality principles
Follow-up TODOs: None - all placeholders resolved
-->

# Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development (SDD) Mandate

**NON-NEGOTIABLE**: All development work MUST follow the Spec-Driven Development workflow. No agent or human may write production code without approved specifications and tasks.

**Required Workflow**:
1. Constitution → Project principles established
2. Specification → Feature requirements documented
3. Plan → Architecture and design decisions recorded
4. Tasks → Implementation broken into testable units
5. Implementation → Code written following approved tasks

**Enforcement Rules**:
- Every feature MUST have an approved `spec.md` before any code is written
- Every feature MUST have an approved `plan.md` documenting architectural decisions
- Every feature MUST have an approved `tasks.md` breaking work into discrete units
- Code reviews MUST verify that implementation matches approved specifications
- Deviations from specifications MUST be resolved by updating the spec, NOT by changing code independently

**Rationale**: SDD ensures predictability, traceability, and quality. It prevents scope creep, reduces rework, and provides clear documentation for all stakeholders. Specifications are the source of truth; code is merely their implementation.

### II. Agent Autonomy with Human Oversight

**Agent Responsibilities**:
- Agents MUST execute tasks autonomously within the bounds of approved specifications
- Agents MUST NOT invent features or requirements beyond what is specified
- Agents MUST NOT make architectural decisions without documenting them in plans
- Agents MUST create Prompt History Records (PHRs) for all significant interactions
- Agents MUST suggest Architecture Decision Records (ADRs) for architecturally significant decisions

**Human Responsibilities**:
- Humans provide requirements, clarifications, and approval
- Humans review and approve specifications, plans, and tasks before implementation
- Humans resolve ambiguities and make final decisions on trade-offs
- Humans MUST NOT write production code manually; agents implement approved specs

**Rationale**: Clear separation of concerns ensures agents can work efficiently while humans maintain strategic control. This prevents manual coding inconsistencies and leverages agent capabilities for implementation speed and consistency.

### III. Phase Governance

The Evolution of Todo project spans five distinct phases, each with defined scope and boundaries:

**Phase Boundaries MUST Be Respected**:
- Each phase MUST be fully specified before implementation begins
- Features from future phases MUST NOT leak into earlier phases
- Phase transitions require explicit specification updates
- Architecture may evolve only through updated specs and plans, not through code changes

**Phase Progression**:
1. **Phase I**: Basic CRUD operations, local database, REST API
2. **Phase II**: User authentication, cloud deployment, advanced features
3. **Phase III**: Real-time collaboration, WebSocket support, multi-tenancy
4. **Phase IV**: Microservices architecture, event-driven patterns, scalability
5. **Phase V**: AI-powered features, advanced analytics, ML integration

**Rationale**: Strict phase boundaries prevent over-engineering, maintain focus, and ensure each phase delivers a working product increment. Future-phase features added prematurely create technical debt and violate the principle of building only what's needed now.

### IV. Refinement at Specification Level

**Specification is the Interface for Change**:
- All feature modifications MUST begin by updating the specification
- Implementation issues discovered during coding MUST be resolved by spec clarification, NOT by agent improvisation
- Architectural improvements MUST be documented in updated plans
- Task breakdowns can be refined, but only if they still implement the approved spec

**Prohibited Actions**:
- Agents MUST NOT "fix" perceived spec deficiencies by adding undocumented features
- Agents MUST NOT make architectural changes without updating plan.md
- Agents MUST NOT deviate from tasks.md without explicit approval
- Code refactoring that changes behavior MUST update specifications first

**Rationale**: Specifications are living documents. Allowing code changes without spec updates creates drift between intent and implementation, making the codebase unmaintainable and unpredictable.

### V. Test-First Development (When Tests Specified)

**Testing Discipline**:
- When tests are specified in tasks.md, they MUST be written before implementation
- Tests MUST fail before implementation begins (Red phase)
- Implementation MUST make tests pass (Green phase)
- Code MUST be refactored only after tests pass (Refactor phase)
- Red-Green-Refactor cycle is strictly enforced for test-driven tasks

**Test Types**:
- **Contract Tests**: Verify API contracts and interfaces remain stable
- **Integration Tests**: Validate component interactions and user journeys
- **Unit Tests**: Test individual functions and classes in isolation

**Optional but Encouraged**:
- Tests are OPTIONAL unless explicitly requested in specifications
- When specified, they are MANDATORY and MUST follow TDD principles
- Test coverage requirements MUST be documented in spec.md if required

**Rationale**: Test-first development catches issues early and ensures code meets requirements. However, not all features require extensive testing; specifications determine testing scope.

### VI. Clean Architecture & Separation of Concerns

**Architectural Principles**:
- **Single Responsibility**: Each module, class, and function has one clear purpose
- **Dependency Inversion**: Depend on abstractions, not concretions
- **Interface Segregation**: Clients should not depend on interfaces they don't use
- **Open/Closed**: Open for extension, closed for modification
- **Layer Separation**: Clear boundaries between presentation, business logic, and data layers

**Code Organization**:
- Models represent business entities
- Services contain business logic
- Controllers/Routes handle API interactions
- Repositories abstract data access
- Libraries provide reusable utilities

**Rationale**: Clean architecture enables maintainability, testability, and scalability. It allows teams to modify one part of the system without cascading changes throughout the codebase.

### VII. Statelessness & Cloud-Native Design

**Stateless Services**:
- Services MUST NOT maintain session state internally
- All state MUST be externalized to databases, caches, or distributed stores
- Services MUST be horizontally scalable
- Idempotency MUST be ensured for non-read operations

**Cloud-Native Patterns**:
- Design for distributed systems from Phase II onwards
- Use managed services where appropriate (databases, caches, queues)
- Implement health checks and graceful shutdown
- Support containerization and orchestration (Docker, Kubernetes in later phases)

**Rationale**: Cloud-native design enables scalability, resilience, and deployment flexibility. Stateless services simplify operations, enable horizontal scaling, and reduce operational complexity.

### VIII. Observability & Operational Excellence

**Logging**:
- Structured logging (JSON format) for all significant events
- Include correlation IDs for request tracing
- Log levels: DEBUG, INFO, WARN, ERROR, CRITICAL
- No sensitive data in logs (passwords, tokens, PII)

**Metrics & Monitoring**:
- Expose health endpoints (/health, /ready)
- Track key metrics (latency, throughput, error rates)
- Implement alerting for critical failures

**Debugging**:
- Clear error messages with actionable guidance
- Stack traces in development, sanitized errors in production
- Correlation IDs for distributed tracing

**Rationale**: Observability enables rapid diagnosis and resolution of issues. Structured logging and metrics provide visibility into system behavior, enabling proactive problem detection and resolution.

## Technology Stack Constraints

### Backend Technology Stack

**Mandatory**:
- **Language**: Python 3.11+
- **Web Framework**: FastAPI
- **ORM**: SQLModel
- **Database**: Neon DB (PostgreSQL-compatible)
- **API Design**: REST (Phase I-II), REST + WebSocket (Phase III+)

**Later Phases**:
- **Event Streaming**: Apache Kafka (Phase IV+)
- **Service Mesh**: Dapr (Phase IV+)
- **AI/ML**: OpenAI Agents SDK (Phase V)
- **MCP**: Model Context Protocol integration (Phase V)

**Rationale**: FastAPI provides modern async Python with automatic API documentation. SQLModel offers type-safe database interactions. Neon DB provides serverless PostgreSQL scalability. Technology choices prioritize developer productivity, type safety, and cloud-native architecture.

### Frontend Technology Stack

**Mandatory (Phase II+)**:
- **Framework**: Next.js (React)
- **Language**: TypeScript
- **State Management**: React Context (Phase II), Redux (if needed Phase III+)
- **Styling**: Tailwind CSS or similar utility-first framework
- **API Client**: Fetch API or Axios

**Rationale**: Next.js provides server-side rendering, static site generation, and excellent developer experience. TypeScript ensures type safety across frontend and backend. React ecosystem provides mature libraries and community support.

### Infrastructure & DevOps

**Mandatory**:
- **Containerization**: Docker (all phases)
- **Orchestration**: Kubernetes (Phase IV+)
- **CI/CD**: GitHub Actions or equivalent
- **Environment Management**: Docker Compose (development), Kubernetes (production Phase IV+)

**Rationale**: Containerization ensures consistency across environments. Kubernetes provides production-grade orchestration. CI/CD automation prevents manual deployment errors and accelerates delivery.

## Development Workflow

### Workflow Stages

1. **Constitution** → Project principles established (this document)
2. **Specification** → Feature requirements documented in `specs/<feature>/spec.md`
3. **Planning** → Architecture designed in `specs/<feature>/plan.md`
4. **Task Breakdown** → Implementation units defined in `specs/<feature>/tasks.md`
5. **Implementation** → Code written by agents following approved tasks
6. **Review** → Human review ensures compliance with specifications
7. **Deployment** → Automated deployment to appropriate environments

### Specification Review Gates

**Before Planning**:
- Specification MUST define clear user scenarios with acceptance criteria
- Functional requirements MUST be testable and unambiguous
- Success criteria MUST be measurable
- Phase boundaries MUST be respected (no future-phase features)

**Before Implementation**:
- Plan MUST document architectural decisions with rationale
- Plan MUST pass constitution compliance checks
- Tasks MUST map to specific user stories
- Tasks MUST include concrete file paths and descriptions
- Dependencies MUST be explicitly documented

**Before Deployment**:
- Implementation MUST match approved specifications
- Tests (if specified) MUST pass
- Code MUST pass linting and formatting checks
- PHRs MUST be created for significant work
- ADRs MUST be created for architectural decisions

### Prompt History Records (PHR)

**Mandatory Recording**:
- PHR MUST be created after every user interaction that results in work
- PHR MUST include full user prompt (verbatim, not truncated)
- PHR MUST include representative agent response
- PHR MUST be routed to appropriate directory based on stage:
  - Constitution work → `history/prompts/constitution/`
  - Feature work → `history/prompts/<feature-name>/`
  - General work → `history/prompts/general/`

**PHR Process**:
1. Detect stage (constitution, spec, plan, tasks, implementation, etc.)
2. Generate descriptive title (3-7 words)
3. Route based on stage (constitution, feature, or general)
4. Use template at `.specify/templates/phr-template.prompt.md`
5. Fill all placeholders (ID, title, stage, dates, prompt, response)
6. Validate no unresolved placeholders remain
7. Report ID, path, stage, and title

**Rationale**: PHRs provide traceability, learning, and historical context. They enable teams to understand why decisions were made and how features evolved over time.

### Architecture Decision Records (ADR)

**Significance Test (All Three Must Be True)**:
1. **Impact**: Does this decision have long-term consequences? (e.g., framework choice, data model design, API design, security model, platform selection)
2. **Alternatives**: Were multiple viable options considered with different trade-offs?
3. **Scope**: Is this decision cross-cutting and does it influence overall system design?

**When to Suggest ADR**:
- When architectural decisions are made during planning or task generation
- When significant technology choices are evaluated
- When trade-offs between approaches are documented
- NEVER auto-create; always suggest and wait for user consent

**ADR Suggestion Format**:
```
📋 Architectural decision detected: [brief-description]
   Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`
```

**Rationale**: ADRs capture the context and rationale behind significant decisions. They prevent repeating past debates and provide future teams with historical context for architectural choices.

## Quality & Architecture Standards

### Code Quality

**Mandatory Practices**:
- No hardcoded secrets or tokens; use environment variables
- Clear error messages with actionable guidance
- No TODO comments without linked issues/tasks
- No commented-out code in production
- Minimal code duplication; extract reusable functions
- Type hints in Python (enforced by mypy)
- TypeScript strict mode in frontend

**Code Style**:
- Python: PEP 8 (enforced by black and ruff)
- TypeScript: ESLint + Prettier
- Meaningful variable and function names
- Functions under 50 lines where practical
- Classes with clear single responsibility

**Rationale**: Consistent code quality reduces bugs, improves maintainability, and accelerates onboarding. Static analysis catches issues before runtime.

### Security Standards

**Authentication & Authorization**:
- JWT tokens for API authentication (Phase II+)
- Role-based access control (RBAC) where needed
- Secrets stored in environment variables or secret management services
- No sensitive data in logs or error messages

**Data Protection**:
- Input validation on all user inputs
- Output encoding to prevent XSS
- SQL injection prevention via ORM (SQLModel parameterized queries)
- HTTPS required for all production traffic (Phase II+)

**Dependency Management**:
- Regular dependency updates
- Vulnerability scanning in CI/CD pipeline
- Pin dependency versions in requirements.txt / package.json

**Rationale**: Security is non-negotiable. Proactive security practices prevent breaches and protect user data.

### Performance Standards

**API Performance**:
- **Phase I**: <500ms p95 latency for CRUD operations (local)
- **Phase II+**: <200ms p95 latency for CRUD operations (cloud)
- **Phase III+**: <100ms p95 for cached reads, <1s for complex queries
- Database query optimization with indexes on frequently queried fields
- Pagination for list endpoints (default 20 items, max 100)

**Frontend Performance**:
- First Contentful Paint (FCP) < 1.5s
- Time to Interactive (TTI) < 3.5s
- Lighthouse score > 90 for performance

**Scalability Targets**:
- **Phase I**: Support 10 concurrent users (development/demo)
- **Phase II**: Support 100 concurrent users
- **Phase III+**: Support 1,000+ concurrent users with horizontal scaling
- **Phase IV+**: Support 10,000+ concurrent users with microservices architecture

**Rationale**: Performance directly impacts user experience. Setting clear targets ensures the system meets user expectations at each phase.

## Governance

### Constitutional Authority

**Supremacy**:
- This constitution supersedes all other project practices, guidelines, or conventions
- In case of conflict, constitution takes precedence
- Amendments require explicit documentation and approval
- All agents and humans MUST comply with constitutional principles

### Amendment Process

**Version Numbering**:
- **MAJOR**: Backward-incompatible governance changes or principle removals
- **MINOR**: New principles added or materially expanded guidance
- **PATCH**: Clarifications, wording improvements, typo fixes

**Amendment Procedure**:
1. Propose amendment with clear rationale
2. Document impact on existing specifications and code
3. Update constitution with version bump
4. Propagate changes to dependent templates (plan, spec, tasks)
5. Create PHR documenting the amendment
6. Communicate changes to all team members

### Compliance & Review

**Continuous Compliance**:
- All pull requests MUST verify compliance with constitution
- Specification reviews MUST check constitutional alignment
- Plan reviews MUST verify architecture follows constitutional principles
- Code reviews MUST ensure implementation matches specifications

**Periodic Reviews**:
- Constitution reviewed quarterly for relevance and clarity
- Metrics tracked: specification compliance rate, PHR completion rate, ADR suggestion rate
- Lessons learned incorporated into constitution updates

### Complexity Justification

**When Complexity is Required**:
- Justify complexity in plan.md with clear rationale
- Document simpler alternatives considered and why they were insufficient
- Link to ADR for significant complexity decisions
- Ensure complexity provides measurable value (performance, scalability, maintainability)

**Prohibited Complexity**:
- Over-engineering for hypothetical future requirements
- Premature optimization without measurements
- Adding features not in specifications
- Using advanced patterns when simple solutions suffice

**Rationale**: Constitution provides predictability and quality standards. Regular reviews ensure it remains relevant as the project evolves. Complexity justification prevents over-engineering.

---

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
