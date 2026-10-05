# Design Failure Mode and Effects Analysis (DFMEA) - Door Trim Substrate

| Item/Function | Potential Failure Mode | Potential Effect of Failure | Severity (S) | Potential Cause | Occurrence (O) | Current Design Controls | Detection (D) | RPN | Recommended Action |
| :--- | :--- | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **B-side Ribs Support** | Sink Marks on Class-A Surface | Poor aesthetic finish, visual quality defect | **7** | Base rib thickness > 60% of nominal wall | **6** | CAD core thickness check module | **3** | **126** | Enforce automated rule checks via `core_rules.py` tool inside design gate |
| **Retainer Attachment** | Door panel detachment / rattling noise | NVH issues, customer complaints | **5** | Excessive spacing between snap attachment doghouses | **4** | CAD structural layout analysis | **4** | **80** | Map strict 150-300mm limit restrictions using optimization script |
