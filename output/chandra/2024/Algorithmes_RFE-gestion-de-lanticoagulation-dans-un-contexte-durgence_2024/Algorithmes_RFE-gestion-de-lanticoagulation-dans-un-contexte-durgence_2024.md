## Algorithme RFE anticoagulation dans un contexte d'urgence

![Logo SFMU (Société Française de Médecine d'Urgence)](2ea5618309a205aa7224ce45a0966b07_2_img.webp)![Logo SFAR (Société Française de Réanimation et de Réanimation Intensive)](2ea5618309a205aa7224ce45a0966b07_3_img.webp)![Logo GIHP (Groupe d'intérêt en hémostase péri-opératoire)](2ea5618309a205aa7224ce45a0966b07_4_img.webp)![Logo SFTH (Société Française de Thrombose et d'Hémostase)](2ea5618309a205aa7224ce45a0966b07_5_img.webp)

<table border="1"><tbody><tr><td></td><td>Hémorragie grave<br/>Procédure à risque hémorragique élevé</td><td></td><td>AVK</td></tr><tr><td></td><td>Hémorragie non grave<br/>Procédure à faible risque hémorragique</td><td></td><td>Dabigatran</td></tr><tr><td></td><td>Seuil</td><td></td><td>Anti-Xa</td></tr><tr><td></td><td>Geste hémostatique</td><td></td><td>HBPM</td></tr><tr><td></td><td>couleur neutre</td><td></td><td>HNF</td></tr></tbody></table>```

graph TD
    A[Hémorragie sous AVK] --> B[Hémorragie grave]
    A --> C[Hémorragie non grave]
    
    B --> D[Geste hémostatique dès que possible]
    D --> E[INR en urgence au laboratoire ou par biologie délocalisée]
    E --> F[Résultat non disponible rapidement]
    E --> G[INR > 1,5 (> 1,2 si hémorragie intracrânienne)]
    E --> H[INR ≤ 1,5 (≤ 1,2 si hémorragie intracrânienne)]
    
    F --> I[CCP 25 UI/kg (1 ml/kg)]
    G --> J[CCP (posologie du RCP)]
    H --> K[Pas de CCP Pas de vitamine K]
    
    I --> L[Vitamine K 10 mg IV ou PO]
    J --> L
    L --> M[INR dans les 30 min]
    
    M --> N[Complément de CCP si INR > 1,5 (> 1,2 si hémorragie intracrânienne) posologie du RCP]
    N --> O[INR à 6-8h et 24h]
    O --> P[Prise en charge selon l'INR et contrôle de l'hémorragie]
    
    C --> Q[Traitement symptomatique et geste hémostatique]
    Q --> R[Rechercher et corriger un surdosage (par vitamine K seule)]
  
```

**Hémorragie sous AVK**

**Hémorragie grave**

Geste hémostatique dès que possible

INR en urgence au laboratoire ou par biologie délocalisée

Résultat non disponible rapidement

INR > 1,5 (> 1,2 si hémorragie intracrânienne)

INR ≤ 1,5 (≤ 1,2 si hémorragie intracrânienne)

CCP 25 UI/kg (1 ml/kg)

CCP (posologie du RCP)

Pas de CCP Pas de vitamine K

Vitamine K 10 mg IV ou PO

INR dans les 30 min

Complément de CCP si INR > 1,5 (> 1,2 si hémorragie intracrânienne) posologie du RCP

INR à 6-8h et 24h

Prise en charge selon l'INR et contrôle de l'hémorragie

**Hémorragie non grave**

Traitement symptomatique et geste hémostatique

Rechercher et corriger un surdosage (par vitamine K seule)

Figure 1```

graph TD
    A[Hémorragie sous dabigatran] --> B[Hémorragie grave]
    A --> C[Hémorragie non grave]
    
    B --> D[Geste hémostatique dès que possible]
    D --> E[Mesure en urgence de la concentration en dabigatran]
    
    E --> F[Résultat non disponible rapidement]
    E --> G["[dabigatran] > 50 ng/mL  
(> 30 ng/mL si hémorragie intracrânienne)"]
    E --> H["[dabigatran] ≤ 50 ng/mL  
(≤ 30 ng/mL si hémorragie intracrânienne)"]
    
    F --> I[Idarucizumab 5 g IV #]
    G --> I
    H --> J[Pas de réversion]
    
    I --> K["Nouvelle mesure [dabigatran] à 12-24h  
si [dabigatran] initiale > 200 ng/mL  
(4-6h si [dabigatran] initiale > 600 ng/mL  
ou CICr < 30 ml/min)"]
    K --> L["± Réadministration d'idarucizumab  
si [dabigatran] > 50 ng/mL  
(> 30 ng/mL si hémorragie intracrânienne),  
selon type et contrôle de  
l'hémorragie"]
    
    C --> M[Traitement symptomatique et geste hémostatique]
    M --> N[Vérifier les modalités du traitement  
(posologie, adaptation à la fonction rénale)]
    
    L --> O["# si idarucizumab indisponible :  
- CCP 50 UI/kg (hémorragie intracrânienne, choc hémorragique)  
- CCP 25-50 UI/kg (autre hémorragie grave)  
- Pas de mesure de [dabigatran] après administration de CCP pour  
vérifier la réversion (car [dabigatran] non modifiée)"]
  
```

**GRADE 2+** (indicated for steps D, E, G, H, I, K, L, N, O)

**AVIS D'EXPERTS** (indicated for steps D, M, O)

**Figure 2**```

graph TD
    Start[Hémorragie sous AOD anti-Xa (rivaroxaban, apixaban, edoxaban)]
    Start --> Grave[Hémorragie grave]
    Start --> NonGrave[Hémorragie non grave]
    
    Grave --> Hemostatic[Geste hémostatique dès que possible]
    Hemostatic --> MeasureAOD[Mesure en urgence de la concentration en AOD anti-Xa]
    MeasureAOD --> ResultNotRapid[Résultat non disponible rapidement]
    MeasureAOD --> AODHigh["[AOD] > 50 ng/mL  
(> 30 ng/mL si hémorragie intracrânienne)"]
    MeasureAOD --> AODLow["[AOD] ≤ 50 ng/mL  
(≤ 30 ng/mL si hémorragie intracrânienne)"]
    
    ResultNotRapid --> CCPDosing["- CCP 50 UI/kg (hémorragie intracrânienne, choc hémorragique)  
- CCP 25-50 UI/kg (autre hémorragie grave)"]
    AODHigh --> CCPDosing
    AODLow --> NoReversal[Pas de réversion]
    
    CCPDosing --> NoMeasureAOD[Pas de mesure [AOD] après administration de CCP pour vérifier la réversion ([AOD] non modifiée)]
    
    NonGrave --> Symptomatic[Traitement symptomatique et geste hémostatique]
    Symptomatic --> CheckModalities[Vérifier les modalités du traitement  
(posologie, adaptation à la fonction rénale)]
  
```

**Hémorragie sous AOD anti-Xa (rivaroxaban, apixaban, edoxaban)**

**Hémorragie grave**

Geste hémostatique dès que possible *AVIS D'EXPERTS*

Mesure en urgence de la concentration en AOD anti-Xa *GRADE 2+*

Résultat non disponible rapidement

[AOD] > 50 ng/mL (*> 30 ng/mL si hémorragie intracrânienne*)

[AOD] ≤ 50 ng/mL (*≤ 30 ng/mL si hémorragie intracrânienne*)

- CCP 50 UI/kg (hémorragie intracrânienne, choc hémorragique)  
- CCP 25-50 UI/kg (autre hémorragie grave) *AVIS D'EXPERTS*

Pas de réversion

Pas de mesure [AOD] après administration de CCP pour vérifier la réversion ([AOD] non modifiée)

**Hémorragie non grave**

Traitement symptomatique et geste hémostatique *AVIS D'EXPERTS*

Vérifier les modalités du traitement (posologie, adaptation à la fonction rénale) *GRADE 2+*

**Figure 3**```

    graph TD
      A[Hémorragie sous HNF à dose curative] --> B[Hémorragie grave]
      A --> C[Hémorragie non grave]
      B --> D[Geste hémostatique dès que possible]
      C --> E[Traitement symptomatique et geste hémostatique]
      D --> F[Hémorragie intracrânienne ou choc hémorragique]
      D --> G[Autre hémorragie grave]
      E --> H[Vérifier absence de surdosage anti-Xa ou TCA]
      F --> I[Protamine cf. Tableau#]
      G --> J[Discuter protamine]
      H --> K[AVIS D'EXPERTS]
      I --> L[GRADE 2+]
      J --> M[AVIS D'EXPERTS]
      K --> N[AVIS D'EXPERTS]
      L --> O[AVIS D'EXPERTS]
      M --> P[AVIS D'EXPERTS]
  
```

**# Posologie du sulfate de protamine**

<table border="1">
<thead>
<tr>
<th>Modalités d'administration de l'HNF</th>
<th>Délai d'administration HNF</th>
<th>Sulfate de protamine</th>
</tr>
</thead>
<tbody>
<tr>
<td>Administration IV continue</td>
<td>/</td>
<td>1 mg pour 100 UI d'HNF administrées dans les 2-3 dernières heures</td>
</tr>
<tr>
<td rowspan="3">Bolus IV unique</td>
<td>&lt; 1 heure</td>
<td>1 mg pour 100 UI d'HNF administrées</td>
</tr>
<tr>
<td>1-3 heures</td>
<td>0,5 mg pour 100 UI d'HNF administrées</td>
</tr>
<tr>
<td>&gt; 3 heures</td>
<td>Pas de réversion</td>
</tr>
<tr>
<td rowspan="3">Administration SC</td>
<td>&lt; 4 heures</td>
<td>1 mg pour 100 UI d'HNF administrées</td>
</tr>
<tr>
<td>4-8 heures</td>
<td>0,5 mg pour 100 UI d'HNF administrées</td>
</tr>
<tr>
<td>&gt; 8 heures</td>
<td>pas de réversion</td>
</tr>
</tbody>
</table>

**Administration du sulfate de protamine :**

- - 1 mg = 100 U.A.H (unités anti-héparine)
- - IV lente sur 10 min, pas de limite de dose
- - Pas de contrôle biologique systématique après protamine.

**Figure 4****Hémorragie sous HBPM à dose curative**

**# Posologie du sulfate de protamine**

<table border="1">
<thead>
<tr>
<th></th>
<th>Dernière administration d'HBPM</th>
<th>Sulfate de protamine</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">tinzaparine, daltéparine</td>
<td>≤ 8 heures</td>
<td>1 mg pour 100 UI d'HBPM administrées</td>
</tr>
<tr>
<td>&gt; 8 heures</td>
<td>Non systématique</td>
</tr>
<tr>
<td rowspan="2">enoxaparine, nadroparine</td>
<td>≤ 8 heures</td>
<td>0,5 mg pour 100 UI d'HBPM administrées.</td>
</tr>
<tr>
<td>&gt; 8 heures</td>
<td>Non systématique</td>
</tr>
</tbody>
</table>

**Administration du sulfate de protamine :**

- - 1 mg = 100 U.A.H (unités anti-héparine)
- - IV lente sur 10 min, pas de limite de dose
- - Pas de contrôle biologique systématique après protamine.

**Figure 5**<table border="1">
<tr>
<td style="background-color: #2e7d62; color: white; text-align: center;">
        INR mesuré<br/><br/>
        INR cible
      </td>
<td style="text-align: center;">INR entre 4 et 6</td>
<td style="text-align: center;">INR entre 6 et 10</td>
<td style="text-align: center;">INR &gt; 10</td>
</tr>
<tr>
<td style="text-align: center;">INR cible 2,5</td>
<td style="text-align: center;">
        Saut d'une prise<br/>
        Adaptation posologique<br/>
<small>GRADE 2+</small><br/>
        Contrôle INR à 48-72h
      </td>
<td style="text-align: center;">
        Saut d'une prise - vit K 2mg per os<br/>
        Adaptation posologique<br/>
<small>GRADE 2+</small><br/>
        Suivi INR toutes les 24-48h
      </td>
<td style="text-align: center;">
        Arrêt AVK – vit K 5mg per os<br/>
        Reprise différée et adaptée<br/>
<small>GRADE 2+</small><br/>
        Suivi INR toutes les 24h
      </td>
</tr>
<tr>
<td style="text-align: center;">
        INR ≥ 3<br/>
        (Fenêtre 2,5-3,5 ou 3-4,5)
      </td>
<td style="text-align: center;">
        Pas de saut de prise<br/>
        Adaptation posologique<br/>
<small>GRADE 2+</small><br/>
        Contrôle INR à 48-72h
      </td>
<td style="text-align: center;">
        Saut d'une prise<br/>
        Adaptation posologique<br/>
<small>GRADE 2+</small><br/>
        Suivi INR toutes les 24h
      </td>
<td style="text-align: center;">
        Arrêt AVK – vit K 2mg per os<br/>
        Reprise différée et adaptée<br/>
<small>GRADE 2+</small><br/>
        Suivi INR toutes les 24h
      </td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">
        Dans tous les cas surveillance clinique* et recherche de l'étiologie †
      </td>
</tr>
</table>

AVIS D'EXPERTS

## Figure 6. Surdosage asymptomatique en AVK

\* Surveillance ambulatoire sauf situation particulière (e.g. haut risque hémorragique, suivi impossible)

† Vérification du schéma posologique et recherche d'un mésusage, d'une insuffisance rénale, d'une co-médication ou d'une intoxication accidentelle.**Procédure invasive non programmée chez un patient traité par AVK**

```

    graph TD
      Start[Procédure invasive non programmée chez un patient traité par AVK] --> HighRisk[Procédure à risque hémorragique élevé  
Seuil: INR ≤ 1,5 (INR ≤ 1,2 si neurochirurgie ou geste neuraxial §)]
      Start --> LowRisk[Procédure à faible risque hémorragique  
réalisable chez un patient anticoagulé]
      
      HighRisk --> Urgent[Procédure urgente  
délai ≤ 12 heures]
      HighRisk --> SemiUrgent[Procédure semi-urgente  
délai > 12 heures]
      
      Urgent --> MeasureINR1[Mesure de l'INR]
      SemiUrgent --> MeasureINR2[Mesure de l'INR]
      
      MeasureINR1 --> ResultNotAvail[Résultat non disponible rapidement]
      MeasureINR1 --> INRgtSeuil1[INR > seuil]
      MeasureINR2 --> INRleSeuil[INR ≤ seuil]
      MeasureINR2 --> INRgtSeuil2[INR > seuil]
      
      ResultNotAvail --> CCP1[CCP  
25 UI/kg (=1ml/kg)#  
+ VitK 5 mg IV ou PO]
      INRgtSeuil1 --> CCP2[CCP  
(posologie du RCP)  
+ VitK 5 mg IV ou PO]
      INRleSeuil --> VitK3[vitK 5 mg IV (ou PO)*]
      INRgtSeuil2 --> VitK3
      
      CCP1 --> ControlINR1[Contrôle de l'INR dans les 30min  
Discuter CCP (posologie du RCP)  
si INR > seuil]
      CCP2 --> ControlINR1
      VitK3 --> ControlINR2[Contrôle de INR à ≥12h  
pour vérifier que le seuil  
est atteint]
      
      ControlINR1 --> Procedure[Realiser la procédure invasive]
      ControlINR2 --> Procedure
      
      Procedure --> Resume[Reprendre une anticoagulation curative (à titre indicatif : entre 24-72h)  
Dans l'intervalle, thromboprophylaxie veineuse si indiquée]
  
```

**GRADE 2+** (High Risk)

**GRADE 1+** (INR Measurement)

**GRADE 1+** (CCP and VitK)

**GRADE 2+** (VitK 5 mg IV)

**GRADE 1+** (Procedure)

**GRADE 1+** (Resume anticoagulation)

\* Discuter 10 mg si procédure à très haut risque hémorragique suivie d'une reprise retardée de l'anticoagulation.

# Les CCP sont dosés en unités de facteur IX.

§ Gestes neuraxiaux : ils incluent la ponction lombaire, la rachianesthésie, la péridurale et la péri-rachi combinée. Ils n'incluent pas la chirurgie rachidienne.

**Figure 7****Procédure invasive non programmée pour un patient traité par anticoagulant oral direct**

**Procédure à risque hémorragique élevé**  
Seuil: [AOD]  $\leq 50$  ng/mL (30 ng/mL si neurochirurgie ou geste neuraxial §)

**Procédure à faible risque hémorragique réalisable chez un patient anticoagulé**

```

graph TD
    Start[Procédure invasive non programmée pour un patient traité par anticoagulant oral direct]
    Start --> HighRisk[Procédure à risque hémorragique élevé  
Seuil: [AOD] ≤50 ng/mL (30 ng/mL si neurochirurgie ou geste neuraxial §)]
    Start --> LowRisk[Procédure à faible risque hémorragique réalisable chez un patient anticoagulé]
    
    HighRisk --> Dabigatran[Dabigatran]
    HighRisk --> AODantiXa[AOD anti-Xa : apixaban, edoxaban, rivaroxaban]
    
    Dabigatran --> DabigatranConc[Mesure de la concentration en dabigatran]
    AODantiXa --> AODantiXaConc[Mesure de la concentration en AOD anti-Xa]
    
    DabigatranConc --> DabigatranConcResult[Résultat non disponible rapidement *]
    DabigatranConc --> DabigatranConcResult[AOD] > seuil *
    DabigatranConc --> DabigatranConcResult[AOD] ≤ seuil
    
    AODantiXaConc --> AODantiXaConcResult[AOD] > seuil *
    AODantiXaConc --> AODantiXaConcResult[Résultat non disponible rapidement *]
    
    DabigatranConcResult[AOD] > seuil * --> Idarucizumab[idarucizumab  
5 g IVL §]
    Idarucizumab --> IdarucizumabConc[Si [dabigatran] avant réversion >200 ng/mL  
Nouvelle mesure 12-24h après idarucizumab]
    IdarucizumabConc --> IdarucizumabConcResult[Si [dabigatran] > seuil de sécurité  
discuter 2ème dose d'idarucizumab  
si risque hémorragique persistant]
    
    AODantiXaConcResult[AOD] > seuil * --> CCP[Discuter les CCP #  
25-50 UI/kg]
    CCP --> CCPResult[- avant la procédure: si nécessité d'une  
hémostase optimale (neurochir...)  
- per procédure: si saignement anormal  
Pas de geste neuraxial §]
    
    AODantiXaConcResult[AOD] ≤ seuil --> Delay[Retarder la  
procédure si cela  
n'entraîne pas une  
perte de chance  
pour le patient]
    
    CCPResult --> Delay
    CCPResult --> ProceedInvasive[Réaliser la procédure invasive]
    Delay --> ProceedInvasive
    
    ProceedInvasive --> Thromboprophylaxie[Thromboprophylaxie veineuse si indiquée]
    Thromboprophylaxie --> Reprise[Reprise de l'anticoagulation curative  
selon le risque hémorragique et thrombotique  
(à titre indicatif entre 24 et 72h)]
    
    LowRisk --> ProceedInvasive
    ProceedInvasive --> Thromboprophylaxie
    Thromboprophylaxie --> Reprise
  
```

**Notes and Explanations:**

- **GRADE 2+:** Indicated for idarucizumab, CCP, and post-procedure thromboprophylaxis.
- **GRADE 1+:** Indicated for the final step of resuming anticoagulation.
- **§:** If unavailable, CCP 25-50 UI/kg according to the same modalities as with AOD anti-Xa.
- **#:** CCP are dosed in units of factor IX.
- **§ Gestes neuraxiaux:** Includes lumbar puncture, spinal anesthesia, epidural, and combined epidural-spinal. Does not include spinal surgery.
- **\*** If the procedure is planned > 12h, take into account the decrease of [AOD] or perform a dosage before the procedure (grade 2+).

**Figure 8****Procédure invasive non programmée pour un patient traité par une héparine (HNF ou HBPM)**

```

graph TD
    Start[Procédure invasive non programmée pour un patient traité par une héparine (HNF ou HBPM)]
    Start --> HighRisk[Procédure à risque hémorragique élevé]
    Start --> LowRisk[Procédure à faible risque hémorragique]
    
    HighRisk --> HNF[Héparine non fractionnée (HNF)]
    HighRisk --> HBPM[Héparines de bas poids moléculaire (HBPM)]
    
    HNF --> ProtamineHNF[Discuter la protamine pour neutraliser l'HNF résiduelle]
    ProtamineHNF --> NoNeuraxialHNF[Pas de geste neuraxial #]
    NoNeuraxialHNF --> Procedure[Réaliser la procédure invasive]
    
    HBPM --> AntiXa[Mesure de l'activité anti-Xa HBPM (+ clairance de la créatinine)]
    AntiXa --> Grade2plus[GRADE 2+]
    Grade2plus --> ActivityHNF[Activité anti-Xa > seuil]
    Grade2plus --> ResultNotAvail[Résultat non disponible]
    Grade2plus --> ActivityHBPMLow[Activité anti-Xa ≤ seuil]
    
    ActivityHNF --> AvisExpertsHNF[AVIS D'EXPERTS]
    AvisExpertsHNF --> Report[Reporter la procédure si cela n'entraîne pas une perte de chance pour le patient de :  
6h si HNF IVSE  
12h si HNF SC  
24h si HBPM SC]
    Report --> AvisExpertsHNF
    AvisExpertsHNF --> Procedure
    
    ResultNotAvail --> Protamine[Discuter la protamine]
    Protamine --> AvisExpertsProt[AVIS D'EXPERTS]
    AvisExpertsProt --> Before[avant la procédure: si nécessité d'une hémostase optimale (neurochir...)]
    AvisExpertsProt --> During[per procédure: si saignement anormal]
    AvisExpertsProt --> NoNeuraxial[Pas de geste neuraxial #]
    NoNeuraxial --> Grade1plus[GRADE 1+]
    Grade1plus --> Procedure
    
    ActivityHBPMLow --> AvisExpertsHBPMLow[AVIS D'EXPERTS]
    AvisExpertsHBPMLow --> Procedure
    
    Procedure --> Thromboprophylaxie[Thromboprophylaxie veineuse si indiquée]
    Thromboprophylaxie --> Reprise[Reprise de l'anticoagulation curative selon le risque hémorragique et thrombotique (à titre indicatif entre 24 et 72h)]
    Reprise --> Grade2plusFinal[GRADE 2+]
  
```

Seuils proposés : Activité anti-Xa >0,2 UI/mL (>0,1 UI/mL si geste neuraxial)

# Gestes neuraxiaux : ils incluent la ponction lombaire, la rachianesthésie, la péridurale et la péri-rachi combinée. Ils n'incluent pas la chirurgie rachidienne. (les délais d'arrêt sont de 6h si HNF IVSE, 12h si HNF SC et 24h si HBPM SC)

**Figure 9****AVC ischémique avec indication à la thrombolyse IV – patient traité par un anticoagulant oral**

![Logo SFMU (Société Française de Médecine d'Urgence)](36dcec3115dfd335fa71af7950777d32_2_img.webp)
![Logo SFAR (Société Française d'Anesthésie et de Réanimation)](36dcec3115dfd335fa71af7950777d32_3_img.webp)
![Logo GIHP (Groupe d'intérêt en hémostasie péri-opératoire)](36dcec3115dfd335fa71af7950777d32_4_img.webp)
![Logo SFTH (Société Française de Thrombose et d'Hémostase)](36dcec3115dfd335fa71af7950777d32_5_img.webp)

```

graph TD
    Start[AVC ischémique avec indication à la thrombolyse IV – patient traité par un anticoagulant oral]
    
    Start --> AVK[AVK]
    Start --> AOD[apixaban, rivaroxaban, edoxaban]
    Start --> Dabi[dabigatran]
    
    AVK --> INR17[INR ≤ 1,7]
    AVK --> INR17n[INR > 1,7 ou dosage non disponible]
    
    INR17 --> Thrombolyse_IV_possible[Thrombolyse IV possible]
    Thrombolyse_IV_possible --> GRADE_1p[GRADE 1+]
    
    INR17n --> Reversal_CCP[Reversion par CCP non recommandée]
    Reversal_CCP --> Avis_Experts[AVIS d'EXPERTS]
    Avis_Experts --> Contre_Indication[Contre indication à la thrombolyse]
    
    AOD --> AOD50[["[AOD] < 50 ng/mL"]]
    AOD --> AOD50_100[["[AOD] ≥ 50 et < 100 ng/mL"]]
    AOD --> AOD100[["Dosage non disponible ou [AOD] ≥ 100 ng/mL"]]
    
    AOD50 --> Thrombolyse_IV_possible
    Thrombolyse_IV_possible --> Avis_Experts
    
    AOD50_100 --> Discuter[Discuter au cas par cas la thrombolyse]
    Discuter --> Avis_Experts
    
    AOD100 --> Reversal_CCP
    Reversal_CCP --> Avis_Experts
    Avis_Experts --> Contre_Indication
    
    Dabi --> Dabi50[["[dabi.] < 50 ng/mL ou TT < 60 sec"]]
    Dabi --> Reversal_Iidarucizumab[Reversion par Idarucizumab]
    
    Reversal_Iidarucizumab --> Oui[Oui]
    Reversal_Iidarucizumab --> Non[Non]
    
    Oui --> Dabi50_100[["[dabi.] ≥ 50 et < 100 ng/mL"]]
    Dabi50_100 --> Discuter
    Discuter --> Avis_Experts
    
    Non --> Dosage_Non_Disponible[["Dosage non disponible ou [dabi.] ≥ 100 ng/mL ou TT ≥ 60 sec"]]
    Dosage_Non_Disponible --> Reversal_CCP
    Reversal_CCP --> Avis_Experts
    Avis_Experts --> Contre_Indication
    
```

Réaliser la thrombectomie si indiquée, quelle que soit la décision de thrombolyse (GRADE 1+)

**Figure 10. Algorithme de prise en charge des patients traités par un anticoagulant oral ayant un AVC ischémique**

AOD : anticoagulants oraux directs, AVK : Anti-Vitamine K, CCP : Concentrés de Complexe Prothrombotique, INR : International Normalized Ratio, IV : intraveineux, TT : temps de thrombine