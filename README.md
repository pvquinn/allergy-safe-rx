# allergy-safe-rx

## Problem:
Accessing allergen information for prescription drugs is difficult for both patients and providers. Providers often do not know the inactive ingredients in medications they prescribe and cannot guide patients in selecting a safe medication. Patients with severe allergies frequently have to check medication safety on their own, leading to increased stress when the patients should be recovering from illness. 

## Proposal:
### Overview:
allergy-safe-rx aims to make _all_ ingredients in medications easily accessible to everyone, even those without a medical background. Users will input the medication needed and the allergens to avoid, and allergy-safe-rx will provide a list of safe prescriptions. 
### Specifications:
Data will be gathered from the DailyMed API available at https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm. allergy-safe-rx will feature a dashboard with inputs for medication names and allergens. Upon submitting, the matching API results without the relevant allergens will be displayed. The safe drugs will be presented with enough information (NPC, brand, dosage, etc.) to prescribe a safe option. Patients can check that their prescriptions are safe in a similar manner.

## Possible expansions:
- Allow search by NPC, drug class, etc.
- Finding substitute medications when the first choice has no safe options
- Integration with EHR systems
  - Restricting providers from prescribing unsafe medications
  - Increasing understanding of patient allergies for emergency providers
  - Virtual access to full medication information for patients
