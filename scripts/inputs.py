BASIC_COLUMNS = [
    "Please provide a link to the resource or tool",
]

UNIQUE_RESOURCE_COLUMNS = ["Who is the author?"]
UNIQUE_TOOLS_COLUMNS = ["What is the name of the tool or resource?"]

RENAMING_DICT = {
    "Who is the author?": "Name",
    "What is the name of the tool or resource?": "Name",
    "Please provide a link to the resource or tool": "Link",
    "Does the resource cover a specific sector?": "Sector",
    "How accessible is this resource?": "Accessibility",
    "What is the purpose of the resource? [Introduction to key concepts of "
    "DMDU]": "Introduction",
    "What is the purpose of the resource? [How-to Guidance to implement a "
    "DMDU analysis]": "How-to Guidance",
    "What is the purpose of the resource? [Serious Game]": "Serious Game",
    "What is the scope of the resource? [Generation of Alternatives ("
    "identifying possible policy actions)]": "Generation of Alternatives",
    "What is the scope of the resource? [Generation of Scenarios ("
    "identifying scenarios to capture different "
    "uncertainties)]": "Generation of Scenarios",
    "What is the scope of the resource? [Robustness Evaluation (evaluating "
    "policy actions across scenarios)]": "Robustness Evaluation",
    "What is the scope of the resource? [Vulnerability Analysis (understand "
    "how policy robustness is affected by uncertainty and "
    "other policies)]": "Vulnerability Analysis",
    "What DMDU methods are covered in the resources? [Robust Decision "
    "Making]": "RDM",
    "What DMDU methods are covered in the resources? [Dynamic Adaptive "
    "Pathways Planning]": "DAPP",
    "What DMDU methods are covered in the resources? [Engineering Options "
    "Analysis]": "EOA",
    "What DMDU methods are covered in the resources? [Info-Gap Theory]": "IG",
    "What DMDU methods are covered in the resources? [Decision-Scaling]": "DS",
    "What level(s) of analysis are covered in the resources? [Qualitative "
    "Analysis]": "Qualitative",
    "What level(s) of analysis are covered in the resources? ["
    "Semi-quantitative Analysis]": "Semi-quantiative",
    "What level(s) of analysis are covered in the resources? [Quantitative "
    "Analysis]": "Quantitative",
    "This this resource contain a case study for illustration?": "Case study",
    "Please provide a short description of the resource": "Short description",
    "Which interface does the tool use?": "Language",
    "How accessible is this tool?": "Accessibility",
    "What is the scope of the tool? [A: prespecified alternatives (evaluate "
    "pre-determined policy alternatives)]": "Prespecified (A)",
    "What is the scope of the tool? [A: iterative generation of alternatives "
    "(start with prespecified policies but refine based on experimental "
    "results)]": "Iterative",
    "What is the scope of the tool? [A: explorative generation of "
    "alternatives (generating policy alternatives from broad ranges of "
    "possible alternatives)]": "Exploration (A)",
    "What is the scope of the tool? [B: prespecified scenarios (capture "
    "specific uncertainty narratives)]": "Prespecified (S)",
    "What is the scope of the tool? [B: explore scenarios (generate "
    "scenarios from a broad range of possibilities)]": "Exploration (S)",
    "What is the scope of the tool? [B: search scenarios (find conseqeuntial"
    " scenarios based on multi-criteria analysis)]": "Search (S)",
    "What is the scope of the tool? [C: evaluate expected  performance "
    "across scenarios]": "Exp. Value",
    "What is the scope of the tool? [C: evaluate higher order moments ("
    "measure variation of performance across scenarios]": "High. Mom.",
    "What is the scope of the tool? [C: evaluate regret (measure deviation "
    "from plausible/best performance]": "Regret",
    "What is the scope of the tool? [C: evaluate satisficing (fraction of "
    "scenarios where performance meets pre-specified requirement)]": "Satisficing",
    "What is the scope of the tool? [D: global sensitivity analysis ("
    "identify relative influence of uncertainties and "
    "policy actions)]": "Global Sensitivity Analysis",
    "What is the scope of the tool? [D: subspace partiotioning (identify "
    "subspaces of scenarios/policy alternatives resulting in similar "
    "outcomes]": "Subspace Partitioning",
    "Please provide a short description of the tool": "Short description",
    "What is the scope of the tool? [A: searching for alternatives (find "
    "high performancing alternatives)]": "Search (A)",
}


CATEGORIES_RESSOURCES = {
    "accessibility": ["Accessibility"],
    "purpose": ["How-to Guidance", "Introduction", "Serious Game"],
    "scope": [
        "Generation of Alternatives",
        "Generation of Scenarios",
        "Robustness Evaluation",
        "Vulnerability Analysis",
    ],
    "methods": ["RDM", "DAPP", "EOA", "IG", "DS"],
    "level analysis": ["Qualitative", "Semi-quantiative", "Quantitative"],
    "case study": ["Case study"],
}

CATEGORIES_TOOLS = {
    "Accessibility": ["Accessibility"],
    "Generation of Alternatives": [
        "Prespecified (A)",
        "Iterative",
        "Exploration (A)",
        "Search (A)",
    ],
    "Generation of Scenarios": ["Prespecified (S)", "Exploration (S)", "Search (S)"],
    "Robustness Evaluation": ["Exp. Value", "High. Mom.", "Regret", "Satisficing"],
    "Vulnerability Analysis": ["Global Sensitivity Analysis", "Subspace Partitioning"],
}


COLORS_RESSOURCES = {
    "accessibility": ["#4d4d4d", "#D3D3D3"],  # dark gray
    "purpose": ["#b28a4d", "#FFE0B3"],  # muted orange-brown
    "scope": ["#4d6fa9", "#CCE0FF"],  # muted navy blue
    "methods": ["#4d994d", "#CCFFCC"],  # muted forest green
    "level analysis": ["#aa4c4c", "#FFCCCC"],  # muted red
    "case study": ["#6f4da9", "#E0CCFF"],  # muted purple
}


COLORS_TOOLS = {
    "Accessibility": ("#4d4d4d", "#D3D3D3"),
    "Generation of Alternatives": ("#3B9AB2", "#CDEBF2"),  # pale cyan
    "Generation of Scenarios": ("#16697A", "#B3DFF0"),  # light sky blue
    "Robustness Evaluation": ("#133C55", "#A6C9E2"),  # light steel blue
    "Vulnerability Analysis": ("#0A1D37", "#9CB3D7"),  # soft navy blue
}
