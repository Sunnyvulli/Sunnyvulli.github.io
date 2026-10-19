# Portfolio presentation redesign

## Goal
Make the engineer, the work, and the supporting evidence legible in a short visit, with a distinct visual identity and useful interactions.

## Direction
Charcoal and ivory with a lime accent; large editorial typography; an interactive engineering illustration; restrained motion; and clear transitions from overview to evidence. The illustration represents a real local project, not a live production dashboard.

## Visitor paths
- Employers: engineering case study, API behavior, tested implementation, experience, resume.
- Faculty/labs: research methods and limitations first, then engineering and teaching evidence, academic CV.
- Preserve `?view=research` and `?view=engineering` deep links, existing document URLs, legacy section anchors, and the research-card update markers.

## Interactions
- Pipeline illustration has three buttons with exposed pressed states and actual project details.
- Project explorer has four tabs, explicit tab/panel relationships, roving tabindex, and arrow/Home/End keyboard navigation.
- Perspective controls update ordering and primary document links; DOM ordering follows visual ordering.
- Section navigation is native-anchor based and works without JavaScript. Default evidence remains visible if scripting fails.
- No fabricated counters, live traffic, production terminal, customer logos, or testimonials.

## Accessibility and verification
Includes semantic headings, native controls, skip navigation, focus styles, reduced-motion rules, readable contrast, responsive CSS, and print styling. Static checks verify unique IDs, local files, fragment targets, ARIA references, JavaScript syntax, and preserved research markers. GitHub CI verifies the existing code, formatter, data evaluations, security history, and container. Visual browser review of the deployed page is performed after publication; responsive CSS does not alone establish mobile browser verification.

## Preservation
Research outcomes, caveats and source/provenance links are preserved from the current publication. The promotional assistance sentence is removed in accordance with the owner's presentation preference; no unaided-authorship claim is introduced. Application PDFs and source code are unchanged.
