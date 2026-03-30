# Code Audit Report
**Date:** March 30, 2026

---

## Project Overview

This is a static HTML/JS quiz app for youth programs (Erasmus+, European Solidarity Corps) with:
- 3 languages (FI, EN, SV)
- 2 result page types (Mobile + Fair/Tablet)
- 6 character types
- Total: 36 result HTML pages + generators

---

## Recent Changes (March 30, 2026)

### ✅ Python Generators Updated - Line Break Fix
- **`generate_results.py`** - Added 18 `<br>` tags to info sections
- **`generate_fair_results.py`** - Added 18 `<br>` tags to info sections

**Why:** Previously, the `<br>` formatting existed in HTML files but was NOT in the Python source files. If someone ran the generators, the line breaks would be lost. Now the Python scripts are the "source of truth" and will preserve formatting on regeneration.

---

## Issues Found

### 1. Duplicate Root HTML Files (Low Priority)
Files in root that may be unused or duplicates:
```
english translations.html
swedsh_transalation.html  (note: typo in filename)
hallintomittari.html
kehittajakehraaja.html
osallisuuskimalainen.html
rohkaisijakuoriainen.html
seikkailijasirkka.html
unelmoijakorento.html
```

**Recommendation:** Verify if root-level HTML files (not in en/fi/sv folders) are needed. They may be old duplicates.

---

### 2. Untracked Files in Git
```
BUG_IPAD_BLACK_TEXT.md
customerfeedback.md
STATUS.md
```

**Recommendation:** Either add to `.gitignore` if not needed, or commit if these are important documentation.

---

### 3. Translation Files Not in Git
Important working documents at root level:
- `english translations.html`
- `swedsh_transalation.html`

**Recommendation:** Either commit these or add to `.gitignore`.

---

### 4. Potential Link Issues (From customerfeedback.md)
- "Erasmus+ nuorisotyöntekijöiden liikkuvuushankkeet" link may not work on some result pages
- Swedish text issue: "att/att" vs "att" (että vs att typo)

---

### 5. External Links Security
STATUS.md notes: External links use `target="_blank"` but should add `rel="noopener noreferrer"`.

**Current status:** Most links already have `rel="noopener noreferrer"` - this appears to be addressed.

---

### 6. Text Content Duplication (Known Issue)
Text exists in 3 places:
1. `js/script.js` (dynamic quiz)
2. `generate_results.py` (mobile pages)
3. `generate_fair_results.py` (fair pages)

**Recommendation:** Consider consolidating to single JSON source in future refactor. See STATUS.md for details.

---

## File Structure

```
/
├── index.html                 (redirects to /fi/)
├── fi/, en/, sv/             (language roots)
│   ├── index.html            (quiz start page)
│   ├── tulokset/             (mobile result pages)
│   │   └── fair/             (tablet result pages with QR codes)
│   ├── tietosuoja.html
│   └── saavutettavuus.html
├── js/
│   └── script.js             (quiz logic)
├── css/
│   └── style.css             (styles)
├── generate_results.py         (generates mobile pages)
├── generate_fair_results.py   (generates fair/tablet pages)
├── assets/
│   └── images/               (character images, logos)
├── BUG_IPAD_BLACK_TEXT.md    (bug documentation)
├── customerfeedback.md        (feedback tracking)
├── STATUS.md                 (project status)
└── CODE_AUDIT.md             (this file)
```

---

## Summary

| Issue | Priority | Status |
|-------|----------|--------|
| Python generators `<br>` fix | High | ✅ Fixed |
| Untracked .md files | Low | Needs decision |
| Duplicate root HTML files | Low | Needs verification |
| Link issues (feedback) | Medium | Needs verification |
| Text duplication | Low | Known issue, future improvement |

---

## Next Steps (If Needed)

1. **Verify link functionality** - Test all external links in result pages
2. **Clean up root files** - Decide if root HTML files are needed
3. **Git ignore** - Add documentation files to .gitignore if not needed
4. **Future refactor** - Consider JSON-based text source to eliminate duplication
