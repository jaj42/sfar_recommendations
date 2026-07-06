```
graph TD; Start([TRAUMATISME]) --> Decision{URGENCE VITALE}; Decision -- OUI --> Rapid[EXTRACTION RAPIDE  
Maintien axe Tête – Cou – Tronc  
(minerve rigide)]; Decision -- NON --> Symptoms[Douleur en regard des apophyses épineuses  
ou  
Troubles de la conscience  
ou  
Déficit neurologique focalisé  
ou  
Alcoolisation, Douleur distractrice]; Symptoms -- NON --> NoImmobil[PAS D'IMMOBILISATION]; Symptoms -- OUI --> PlanImmobil[EXTRACTION PLAN DUR  
IMMOBILISATION CERVICALE  
(Fixateur de tête)]; PlanImmobil --> Transport([Transport matelas coquille]);
```

The flowchart begins with an oval labeled 'TRAUMATISME'. An arrow points down to a red diamond labeled 'URGENCE VITALE'. From the diamond, two arrows branch out: one labeled 'OUI' leading to an orange box 'EXTRACTION RAPIDE' with the text 'Maintien axe Tête – Cou – Tronc (minerve rigide)'; the other labeled 'NON' leading to a vertical stack of four purple boxes. These boxes contain: 'Douleur en regard des apophyses épineuses', 'ou', 'Troubles de la conscience', 'ou', 'Déficit neurologique focalisé', 'ou', and 'Alcoolisation, Douleur distractrice'. From the bottom of the stack, two arrows branch out: one labeled 'NON' leading to an orange box 'PAS D'IMMOBILISATION'; the other labeled 'OUI' leading to an orange box 'EXTRACTION PLAN DUR IMMOBILISATION CERVICALE (Fixateur de tête)'. Finally, an arrow from the last box points down to a grey oval labeled 'Transport matelas coquille'.

Algorithme sur l'immobilisation rachidienne des patients avec ou à risque de lésion médullaire cervicale (Avis d'experts)```

graph TD
    Start([Indication d'intubation trachéale d'un patient avec ou à risque de lésion médullaire cervicale])
    Start --> Extra{Intubation en milieu EXTRA-HOSPITALIER}
    Start --> Hospital{Intubation en milieu HOSPITALIER}
    
    Extra --> Box1[1) Induction séquence rapide  
2) LARYNGOSCOPIE DIRECTE  
3) MANDRIN LONG (type Eschmann)  
4) Stabilisation du rachis en ligne]
    
    Hospital --> Vital{URGENCE VITALE}
    Vital -- NON --> EP[Estomac plein (EP)]
    EP -- NON --> Mouth[Ouverture de bouche limitée  
ou  
Ventilation au masque prévue difficile]
    Mouth -- OUI --> Box2[1) Intubation fibroscopique en ventilation spontanée  
2) Stabilisation du rachis en ligne]
    
    Vital -- OUI --> Box3[1) Induction séquence rapide (si Estomac Plein ou urgence vitale)  
2) VIDEOLARYNGOSCOPIE  
3) Stabilisation du rachis en ligne]
    EP -- OUI --> Box3
    Mouth -- NON --> Box3
  
```

The flowchart outlines the procedure for tracheal intubation in patients with a risk of cervical spinal cord injury. It starts with the indication of intubation, branching into two main paths: **Extra-Hospitalier** and **Hospitalier**.

- **Extra-Hospitalier:** Leads to a box containing:
  1. 1) Induction séquence rapide
  2. 2) LARYNGOSCOPIE DIRECTE
  3. 3) MANDRIN LONG (type Eschmann)
  4. 4) Stabilisation du rachis en ligne
- **Hospitalier:** Leads to a decision diamond **URGENCE VITALE**.
  - If **NON** (not vital emergency):
    - Check **Estomac plein (EP)**.
      - If **NON**: Proceed to **Ouverture de bouche limitée** or **Ventilation au masque prévue difficile**. If **OUI**, proceed to:
        1. 1) Intubation fibroscopique en ventilation spontanée
        2. 2) Stabilisation du rachis en ligne
      - If **OUI**: Proceed to the common box below.
  - If **OUI** (vital emergency): Proceed directly to the common box below.

**Common Path (from Vital Emergency or EP OUI):**

- 1) Induction séquence rapide (si Estomac Plein ou urgence vitale)
- 2) VIDEOLARYNGOSCOPIE
- 3) Stabilisation du rachis en ligne

Algorithme : Procédure de l'intubation trachéale chez les patients avec ou à risque de lésion médullaire cervicale (Avis d'Experts)