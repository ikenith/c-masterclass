with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

diagram_css = """
/* ==========================================================================
   Interactive & Visual Pedagogical Diagrams (Flowcharts, Bitwise, Pipelines)
   ========================================================================== */

/* 1. Visual Flowchart Nodes & Diagram Engine */
.visual-flowchart {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin: 1.5rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
  box-shadow: var(--shadow-sm);
  overflow-x: auto;
}

.fc-node {
  padding: 0.65rem 1.25rem;
  text-align: center;
  font-family: var(--font-heading);
  font-weight: 600;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.45rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  transition: transform 0.2s ease;
  max-width: 90%;
  position: relative;
}

.fc-node:hover {
  transform: scale(1.03);
}

/* Shapes */
.fc-node.terminal {
  border-radius: var(--radius-full);
  background: linear-gradient(135deg, #10b981, #059669);
  color: #fff;
  min-width: 140px;
}

.fc-node.io {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  color: #fff;
  border-radius: 4px;
  transform: skew(-12deg);
  min-width: 180px;
}
.fc-node.io > * {
  transform: skew(12deg);
}

.fc-node.process {
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #fff;
  border-radius: var(--radius-sm);
  min-width: 200px;
}

.fc-node.decision {
  background: linear-gradient(135deg, #8b5cf6, #7c3aed);
  color: #fff;
  border-radius: 6px;
  min-width: 180px;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.fc-arrow {
  color: var(--text-muted);
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 1.25rem;
}

.fc-decision-branches {
  display: flex;
  justify-content: center;
  gap: 2rem;
  width: 100%;
  margin-top: 0.5rem;
}

.fc-branch {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  max-width: 260px;
  padding: 0.75rem;
  background: var(--bg-surface);
  border: 1px dashed var(--border-strong);
  border-radius: var(--radius-md);
}

.fc-branch-tag {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 0.2rem 0.6rem;
  border-radius: var(--radius-full);
}
.fc-branch-tag.true-tag { background: rgba(16, 185, 129, 0.2); color: var(--accent-emerald); }
.fc-branch-tag.false-tag { background: rgba(244, 63, 94, 0.2); color: var(--accent-rose); }

/* 2. The Rosetta Stone (English <-> Pseudocode <-> C Code) */
.rosetta-bridge {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}

.rosetta-col {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.rosetta-header {
  padding: 0.6rem 1rem;
  font-size: 0.78rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.rosetta-header.english { background: rgba(59, 130, 246, 0.15); color: var(--accent-blue); }
.rosetta-header.pseudocode { background: rgba(168, 85, 247, 0.15); color: var(--accent-purple); }
.rosetta-header.c-code { background: rgba(16, 185, 129, 0.15); color: var(--accent-emerald); }

.rosetta-body {
  padding: 1rem 1.1rem;
  font-size: 0.88rem;
  line-height: 1.5;
  color: var(--text-secondary);
  flex: 1;
}

.rosetta-body pre {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  background: var(--code-bg);
  padding: 0.75rem;
  border-radius: var(--radius-sm);
  color: #e6edf3;
  overflow-x: auto;
}

/* 3. Bitwise Alignment Matrix */
.bit-matrix-card {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  margin: 1.5rem 0;
  overflow-x: auto;
}

.bit-matrix-title {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.45rem;
}

.bit-matrix-table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-mono);
  font-size: 0.9rem;
  text-align: center;
}

.bit-matrix-table td {
  padding: 0.45rem 0.6rem;
  border-bottom: 1px solid var(--border-subtle);
}

.bit-matrix-table .row-label {
  text-align: left;
  font-weight: 600;
  color: var(--text-muted);
  font-size: 0.8rem;
  white-space: nowrap;
}

.bit-matrix-table .bit-cell {
  background: var(--bg-surface);
  border-radius: 4px;
  font-weight: 700;
  min-width: 28px;
}

.bit-matrix-table .bit-cell.highlight {
  background: rgba(59, 130, 246, 0.25);
  color: var(--accent-cyan);
  border: 1px solid var(--accent-blue);
}

.bit-matrix-table .bit-cell.zero {
  color: var(--text-muted);
}

.bit-matrix-table .bit-result-cell {
  background: rgba(16, 185, 129, 0.2);
  color: var(--accent-emerald);
  font-weight: 700;
  border: 1px solid var(--accent-emerald);
  border-radius: 4px;
}

/* 4. Binary Power-of-2 Weight Buckets */
.weight-buckets {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding: 0.5rem 0;
  margin: 1rem 0;
}

.bucket-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  min-width: 38px;
  flex: 1;
}

.bucket-weight {
  font-size: 0.72rem;
  font-family: var(--font-mono);
  color: var(--accent-amber);
  font-weight: 700;
}

.bucket-power {
  font-size: 0.65rem;
  color: var(--text-muted);
}

.bucket-bit {
  width: 100%;
  height: 36px;
  background: var(--bg-surface-elevated);
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--text-secondary);
}

.bucket-bit.active-one {
  background: rgba(59, 130, 246, 0.3);
  border-color: var(--accent-blue);
  color: var(--accent-cyan);
  box-shadow: 0 0 10px var(--accent-blue-glow);
}

/* 5. Radix Conversion Ladder */
.conversion-ladder {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 1.25rem;
  margin: 1rem 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
}

.ladder-col h5 {
  font-family: var(--font-heading);
  font-size: 0.9rem;
  color: var(--accent-cyan);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.ladder-step {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.4rem 0.6rem;
  border-bottom: 1px dashed var(--border-subtle);
  font-family: var(--font-mono);
  font-size: 0.82rem;
}

.ladder-step .calc { color: var(--text-secondary); }
.ladder-step .rem { color: var(--accent-emerald); font-weight: 700; }

/* 6. Compilation Conveyor Pipeline */
.conveyor-pipeline {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  overflow-x: auto;
  padding: 1rem 0;
  margin: 1.5rem 0;
}

.conveyor-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  padding: 0.85rem 1rem;
  min-width: 140px;
  text-align: center;
  box-shadow: var(--shadow-sm);
  flex-shrink: 0;
}

.conveyor-tool {
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--accent-cyan);
  text-transform: uppercase;
  margin-bottom: 0.25rem;
}

.conveyor-name {
  font-family: var(--font-heading);
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.conveyor-ext {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  background: var(--bg-surface);
  color: var(--accent-amber);
  border: 1px solid var(--border-subtle);
}

.conveyor-arrow {
  color: var(--text-muted);
  font-size: 1.1rem;
  flex-shrink: 0;
}

/* ==========================================================================
   Mobile-First Refinements (Phones & Tablets)
   ========================================================================== */
@media (max-width: 768px) {
  :root {
    --header-height: 60px;
    --footer-height: 70px;
  }

  .site-header {
    padding: 0 0.85rem;
  }

  .brand-logo {
    width: 34px;
    height: 34px;
    font-size: 1rem;
  }

  .brand-title {
    font-size: 0.95rem;
  }

  .brand-subtitle {
    display: none;
  }

  .main-content {
    padding: 0.75rem 0.75rem 5rem 0.75rem;
  }

  .timeline-section {
    padding: 1rem;
    border-radius: var(--radius-md);
    margin-bottom: 1.25rem;
  }

  .timeline-header h2 {
    font-size: 1rem;
  }

  .lesson-card {
    padding: 1.25rem 1rem;
    border-radius: var(--radius-md);
  }

  .lesson-title {
    font-size: 1.35rem;
    line-height: 1.3;
  }

  .lesson-subtitle {
    font-size: 0.9rem;
  }

  .teacher-callout {
    flex-direction: column;
    gap: 0.5rem;
    padding: 1rem;
  }

  .callout-icon {
    font-size: 1.2rem;
  }

  .fc-decision-branches {
    flex-direction: column;
    gap: 1rem;
  }

  .fc-branch {
    max-width: 100%;
  }

  .rosetta-bridge {
    grid-template-columns: 1fr;
  }

  .bottom-action-bar {
    height: var(--footer-height);
    padding: 0 0.75rem;
  }

  .action-btn {
    padding: 0.55rem 0.85rem;
    font-size: 0.8rem;
  }

  .action-bar-center {
    gap: 0.4rem;
  }

  .modal-container.large,
  .modal-container.medium {
    width: 100vw;
    height: 100vh;
    max-height: 100vh;
    border-radius: 0;
  }

  .modal-header {
    padding: 1rem;
  }

  .modal-body {
    padding: 1rem;
  }

  .converter-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 420px) {
  .action-btn.complete span {
    display: none;
  }
  .action-btn.prev, .action-btn.next {
    padding: 0.5rem 0.65rem;
  }
}
"""

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css + "\n" + diagram_css)

print("Visual diagram styles and enhanced mobile responsiveness added to style.css!")
