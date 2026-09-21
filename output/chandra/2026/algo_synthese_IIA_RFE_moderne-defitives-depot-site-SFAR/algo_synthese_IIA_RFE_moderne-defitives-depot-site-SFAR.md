![Gear icon representing settings or configuration.](f725f7734dc878dd0d726539cb303b77_1_img.webp)

## IIA COMMUNAUTAIRE

```
graph TD; Start(( )) --> Allergy{Allergie aux β-lactamines ?}; Allergy -- "✓ OUI" --> AllergyOptions["Lévofloxacine + Métronidazole  
ou Moxifloxacine *  
ou Tigécycline ou Eravacycline #"]; Allergy -- "✗ NON" --> Shock{État de choc ?}; Shock -- "✗ NON" --> ShockOptions["Céfotaxime ou Ceftriaxone  
+ Métronidazole"]; Shock -- "✓ OUI" --> Risk{Facteurs de risque  
de BLSE ?}; Risk -- "✗ NON" --> RiskOptions["Pipéracilline / tazobactam"]; Risk -- "✓ OUI" --> Carbapenems["Carbapénèmes"]; AllergyOptions --> Experts["AVIS D'EXPERTS"]; ShockOptions --> Grade2["GRADE 2"]; RiskOptions --> Grade2["GRADE 2"]; Carbapenems --> Grade2["GRADE 2"];
```

**Allergie aux β-lactamines ?**

- **✓ OUI**: Lévofloxacine + Métronidazole  
  ou Moxifloxacine \*  
  ou Tigécycline ou Eravacycline #
- **✗ NON**: Proceed to **État de choc ?**

**État de choc ?**

- **✗ NON**: Céfotaxime ou Ceftriaxone + Métronidazole
- **✓ OUI**: Proceed to **Facteurs de risque de BLSE ?**

**Facteurs de risque de BLSE ?**

- **✗ NON**: Pipéracilline / tazobactam
- **✓ OUI**: Carbapénèmes

**AVIS D'EXPERTS**

**GRADE 2**

![Gear icon representing settings or configuration.](f725f7734dc878dd0d726539cb303b77_4_img.webp)

### Facteurs de risque de BLSE

- • ATCD d'infection / colonisation à BLSE < 6 mois
- • Amoxicilline-ac. clavulanique, C2G/C3G ou fluoroquinolone < 6 mois
- • Voyage en zone d'endémie < 3 mois
- • Institution médico-sociale (EHPAD, SLD) + dispositif invasif permanent
- • ou prévalence locale élevée# IIA ASSOCIÉE AUX SOINS

```

graph TD
    Start([IAA ASSOCIÉE AUX SOINS]) --> Allergy{Allergie aux β-lactamines ?}
    Allergy -- "✓ OUI" --> AllergyOptions["Ciprofloxacine + métronidazole  
ou Aztréonam + métronidazole  
ou Tigécycline / éravacycline  
+ ciprofloxacine *"]
    Allergy -- "✗ NON" --> RiskBMR{Facteurs de risque de BMR ?}
    RiskBMR -- "✗ NON" --> RiskBMRYes{Facteurs de risque de BMR ?}
    RiskBMRYes -- "✓ OUI" --> RiskBMRNo["Céfépime + métronidazole  
Pipéracilline-tazobactam"]
    RiskBMR -- "✓ OUI" --> RiskBMRNo
    RiskBMRNo --> RiskEnterococcus{Facteurs de risque d'entérocoque AmpiR ?}
    RiskEnterococcus -- "✓ OUI" --> RiskEnterococcusNo["Imipénème ou méropénème"]
    RiskEnterococcus -- "✗ NON" --> RiskEnterococcusNo
    RiskEnterococcusNo --> AddEnterococcus["+ Linézolide ou Vancomycine ou Teicoplanine  
à ajouter à tous les régimes précédents (sauf *)"]
    RiskEnterococcusNo --> AddEnterococcus
    
```

**Facteurs de risque de BMR**

- C3G ou fluoroquinolone < 3 mois ; portage < 3 mois de BLSE ou P. aeruginosa CAZ-R
- Hospitalisation à l'étranger < 12 mois ; institution médico-sociale + dispositif invasif
- Échec ou récidive < 15 j après C3G, fluoroquinolone ou pip-tazo (≥ 3 j)

**FdR d'entérocoque AmpiR**

- Point de départ hépato-biliaire ; transplantation hépatique ; immunodépression
- Patient déjà sous antibiothérapie ou C3G préalable

**Antibiotic Regimens:**

- **Grade 1:** Céfépime + métronidazole
- **Grade 2:** Pipéracilline-tazobactam
- **Grade 2:** Imipénème ou méropénème
- **Additional:** Linézolide ou Vancomycine ou Teicoplanine à ajouter à tous les régimes précédents (sauf \*)

![Gear icon representing risk factors.](aa725b2d7b4d8d43a2acd1faceb72286_3_img.webp)

## Facteurs de risque de BMR

- C3G ou fluoroquinolone < 3 mois ; portage < 3 mois de BLSE ou P. aeruginosa CAZ-R
- Hospitalisation à l'étranger < 12 mois ; institution médico-sociale + dispositif invasif
- Échec ou récidive < 15 j après C3G, fluoroquinolone ou pip-tazo (≥ 3 j)

![Gear icon representing risk factors.](aa725b2d7b4d8d43a2acd1faceb72286_6_img.webp)

## FdR d'entérocoque AmpiR

- Point de départ hépato-biliaire ; transplantation hépatique ; immunodépression
- Patient déjà sous antibiothérapie ou C3G préalable

![Shoe icon indicating expert advice.](aa725b2d7b4d8d43a2acd1faceb72286_9_img.webp)

Ciprofloxacine + métronidazole  
ou Aztréonam + métronidazole  
ou Tigécycline / éravacycline  
+ ciprofloxacine \*

AVIS D'EXPERTS

![Shoe icon indicating expert advice.](aa725b2d7b4d8d43a2acd1faceb72286_12_img.webp)

Céfépime + métronidazole

GRADE 1

![Shoe icon indicating expert advice.](aa725b2d7b4d8d43a2acd1faceb72286_15_img.webp)

Pipéracilline-tazobactam

AVIS D'EXPERTS

![Shoe icon indicating expert advice.](aa725b2d7b4d8d43a2acd1faceb72286_18_img.webp)

Imipénème ou méropénème

GRADE 2

![Plus sign icon indicating addition of a regimen.](aa725b2d7b4d8d43a2acd1faceb72286_21_img.webp)
![Plus sign icon indicating addition of a regimen.](aa725b2d7b4d8d43a2acd1faceb72286_22_img.webp)

Linézolide ou Vancomycine ou Teicoplanine  
à ajouter à tous les régimes précédents (sauf \*)

AVIS D'EXPERTS![Gear icon representing a process or setting.](c7568cbccbea03f25227209c08cbedb9_1_img.webp)

# INFECTION INTRA-ABDOMINALE

![Icon of a person wearing a stethoscope.](c7568cbccbea03f25227209c08cbedb9_3_img.webp)

## Endossement RFE SFAR 2015

**R21** — patient grave (IIA communautaire ou associée aux soins) : si antifongique probabiliste décidé, utiliser une échinocandine.

**R41** — IIA associée aux soins : antifongique probabiliste si levure à l'examen direct ou culture péritonéale positive (échinocandine si infection grave ou souche fluconazole-R).

![Information icon (i).](c7568cbccbea03f25227209c08cbedb9_7_img.webp)

### Peritonitis Score (1 pt / critère)

- • Défaillance hémodynamique
- • Sexe féminin
- • Chirurgie sus-mésocolique
- • Antibiothérapie > 48 h

```
graph TD; Start([INFECTION INTRA-ABDOMINALE]) --> D1{Examen direct positif à levure  
ou Peritonitis Score ≥ 3}; D1 -- "X NON" --> NoAntifongique[Pas de traitement antifongique]; D1 -- "✓ OUI" --> D2{Défaillance hémodynamique  
ou IIA associée aux soins}; D2 -- "X NON" --> NoAntifongique; D2 -- "✓ OUI" --> D3{Facteur de risque de souche résistante  
au fluconazole  
ou complication postopératoire  
après IIA}; D3 -- "X NON" --> Fluconazole[Fluconazole]; D3 -- "✓ OUI" --> Echinocandine[Échinocandine];
```

The flowchart outlines the treatment protocol for intra-abdominal infection. It begins with a decision point: 'Examen direct positif à levure ou Peritonitis Score ≥ 3'. If 'NON' (No), the treatment is 'Pas de traitement antifongique' (No antifungal treatment). If 'OUI' (Yes), the next decision is 'Défaillance hémodynamique ou IIA associée aux soins'. If 'NON', it leads to 'Pas de traitement antifongique'. If 'OUI', the final decision is 'Facteur de risque de souche résistante au fluconazole ou complication postopératoire après IIA'. If 'NON', the treatment is 'Fluconazole'. If 'OUI', the treatment is 'Échinocandine'.