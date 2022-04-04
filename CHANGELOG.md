teleservices-package changelog
==============================
:App involved: iA.Téléservices, Publik
:Info: This is the changelog for the teleservices-package
:Authors: Daniel Muyshond, Nicolas Hislaire, Nicolas Selva
:License: GNU Affero General Public License v3 or later (AGPLv3+)
## [0.1.47] - 04-04-2022 -
### Updated
  - [TELE-1134] fix category of Acte de Reconnaissance pré/post-natale

## [0.1.47] - 04-04-2022 -
### Updated
  - [TELE-1288] updated forms Candidature validation nrn

## [0.1.47] - 04-04-2022 -
### Updated
  - [TELE-1288] updated forms Population validation nrn

## [0.1.47] - 04-04-2022 -
### Updated
  - [TELE-1288] updated forms Actes validation nrn

## [0.1.46] - 30-03-2022 -
### Updated
  - [TELE-1282] updated forms Pouplation Description

## [0.1.46] - 30-03-2022 -
### Updated
  - [TELE-1282] updated forms Etat-Civil Description

## [0.1.46] - 30-03-2022 -
### Updated
  - [TELE-1164] updated form Acte de Reconnaissance pré/post-natale

## [0.1.46] - 30-03-2022 -
### Fixed
  - [TELE-1148] updated commentaire in Candidature poste à pourvoir

## [0.1.46] - 30-03-2022 -
### Fixed
  - [TELE-1154] fixed commentaire in Certificat de vie

## [0.1.46] - 30-03-2022 -
### Fixed
  - [TELE-1283] fixed condition in Occupation de la voie publique 

## [0.1.45] - 01-01-2022 -
### update
  - [SUP-21926] update webservice réservation agenda for rappel 

## [0.1.45] - 01-01-2022 -
### Added
  - [TELE-1238] add new wf for pin/puk form and update its form


## [0.1.44] - 24-01-2022 -
### Fixed
  - [TELE-1226] fix spelling mistake in status name  [dmshd]
  - [TELE-1226] fix order of actions making a mail action is not played (mail not sent) [dmshd]

## [0.1.43] - 18-01-2022 -
### Fixed
  - [TELE-1207] add datasources and carddefs for new "motifs" and "modes d'envoi" using cards  [dmshd]

## [0.1.42] - 13-12-2021 -
### Fixed
  - [TELE-1182] add hint in forms and blocs for list item  [NSE]

## [0.1.41] - 23-11-2021 -
### Fixed
  - [TELE-1163] remove hard burdinne in workflow  [nhi]

## [0.1.40] - 22-11-2021 -
### Fixed
  - [TELE-1158] fix spelling mistake [dmshd]

## [0.1.39] - 25-10-2021 -
### Fixed
   - add pays in data_source

## [0.1.38] - 25-10-2021 -
### Fixed
   - add motifs and destinations in data_source

## [0.1.37] - 19-10-2021 -
### Fixed
   - [TELE-1144] set install path in jenkinsfile [nhi]

## [0.1.36] - 18-10-2021 -
### Updated
   - set version in setup.py
   - use iateleservicesCreateDeb pipeline function

## [0.1.35] - 18-10-2021 -
### Updated
   - workflow-imio-gestion-des-rendez-vous-et-evenements-package with guichet

## [0.1.34] - 18-10-2021 -
### Removed
   - BAEC option in [dmshd]

## [0.1.33] - 14-10-2021 -
### Fixed
   - [TELE-1135] Fix spelling mistake in two variables inside two conditions [dmshd]

## [0.1.32] - 14-10-2021 -
### Fixed
   - [TELE-1128] Fix links not working because of protocol set to "http" [dmshd]

## [0.1.31] - 14-10-2021 -
### Added
   - Install usage in README [dmshd]

## [0.1.30] - 05-10-2021 -
### Fixed
   - Fix typo in subject of refus mail in WF dep. citoyen

## [0.1.29] - 05-10-2021 -
### Fixed
   - Fix subject of refus mail in WF dep. citoyen

## [0.1.28] - 05-10-2021 -
### Fixed
   - Do not verify SSL certificate's validity
   - Fix motif refus display in mail in WF dep. citoyen
   - Re order auto-jumps for refund in WF dep. citoyen

## [0.1.27] - 28-09-2021 -
### Fixed
   - Fix total amount if a coma is used instead of a dot

## [0.1.26] - 24-09-2021 -
### Fixed
   - Ghost mail template in wf iMio - Changement d'adresse

## [0.1.25] - 23-09-2021 -
### Fixed
   - category of euthanasia's form

## [0.1.24] - 22-09-2021 -
### Updated
   - all forms
   - all workflows
   - all mail-templates
   - all blocks

## [0.1.23] - 22-09-2021 -
### Fix
   - missing xml tag
### Removed
   - one more option in forms

## [0.1.22] - 22-09-2021 -
### Removed
   - all roles and most prefill options in forms

## [0.1.21] - 21-09-2021 -
### Updated
   - all forms
   - all workflows
   - all mail-templates
   - all blocks

## [0.1.20] - 13-09-2021 -
### Updated
  - wf with paiement alert

## [0.1.19] - 13-09-2021 -
### Updated
  - wf paiement with pk button basket

## [0.1.18] - 07-09-2021 -
### Updated
  - form changement d'adresse with instruction
  - category

## [0.1.17] - 07-09-2021 -
### Updated
  - wf changement d'adresse

## [0.1.16] - 07-09-2021 -
### Updated
  - form radiation pour l'étranger

## [0.1.15] - 30-08-2021 -
### Updated
  - pop etat-civil form's with mode d'emploi

## [0.1.14] - 26-08-2021 -
### Updated
  - wf iMio - Gestion des rendez-vous et événements - package with documentation
  - forms acte with redirection mondossier
  - some form's name with Demande
  - a mail template in workflow-imio-changement-d-adresse
  - url name et internal identifier for all form
  - name files of all form
  - all form's name
### Merged
  - doublon enseignement communal

## [0.1.12] - 11-08-2021 -
### Updated
  - wf Chien dangereux
  - wf document pdf
### Added
  - mode d'emploi on Finance and Logement forms
  - mode d'emploi chien dangereux
  - mode d'emploi on Environement forms
  - Mode d'emploi on euthanasie form
### Patched
  - card candidature poste à pourvoir slug's
  - candidature cards slug's
  - form imio compteur d'eau champ société

## [0.1.11] - 09-08-2021 -
### Disabled
  - all forms
### Updated
  - form and wf chien dangereux
  - form and wf demande d'occuptation de la voie publique
  - form Déclaration de résidence secondaire
  - lien mondossier in form Acte
  - form changement d'adresse
  - block-identite_changement_adresse.wcs
  - form acte de nationalité
  - workflow for radiation pour l'étranger
  - form certificat de radiation
  - wf departement citoyen
  - form candidature spontanée
### Patched
  - remove data source motif and destination
  - form_option_cp in cohabitation legale and radiation pour l'étranger
### Added
  - Cards lien vers formulaire

## [0.1.9] - 05-08-2021 -
### Updated
  - forms iMio from category emplois
### Patched
  - forms redirection with correct wf

## [0.1.8] - 29-07-2021 -
### Patched
  - forms iMio - Redirection Modele link to workflow

## [0.1.7] - 29-07-2021 -
### Patched
  - cards

## [0.1.6] - 28-07-2021 -
### Updated
  - form iMio - Candidature spontanée

## [0.1.5] - 27-07-2021 -
### Updated
  - localite in iMio - Demande d'occupation de la voie publique

## [0.1.4] - 27-07-2021 -
### Patched
  - error message rn
  - regex rn

## [0.1.3] - 27-07-2021 -
### Patched
  - condition rn

## [0.1.2] - 27-07-2021 -
### Patched
  - View of card card-imio-candidature-pour-l-enseignement-communal-fonctions-disponibles

## [0.1.1] - 26-07-2021 -
### Patched
  - View of card card-imio-candidature-pour-l-enseignement-communal-fonctions-disponibles

## [0.1.0] - 26-07-2021 -
### Updated
  - form form-imio-candidature-enseignement-communal
### Added
  - carddefs for fonction in this form
  [nse]

## [0.0.55] - 12-07-2021 -
### Updated
  - forms internal identifier
  [nse]

## [0.0.54] - 12-07-2021 -
### Updated
  - form iMio - Déclaration de chien dangereux
  [nse]

## [0.0.53] - 12-07-2021 -
### Added
  - description to forms
### Updated
  - change blocs de champs name
  [nse]

## [0.0.52] - 06-07-2021 -
### deleted
  - url name from all forms
  [nse]

## [0.0.50] - 06-07-2021 -
### updated
  - agenda forms name
  [nse]

## [0.0.49] - 06-07-2021 -
### Added
  - Modele coordonées
  [nse]

## [0.0.48] - 06-07-2021 -
### Patched
  - category of redirection forms
  [nse]

## [0.0.47] - 05-07-2021 -
### Patched
  - category of some forms
  - name of some forms
  [nse]

## [0.0.46] - 05-07-2021 -
### Patched
  - category of some forms
  [nse]

## [0.0.45] - 05-07-2021 -
### Updated
  - category url_name
  [nse]

## [0.0.44] - 05-07-2021 -
### Updated
  - category id
  [nse]

## [0.0.43] - 05-07-2021 -
### Updated
  - change file name forms
  [nse]

## [0.0.42] - 05-07-2021 -
### Updated
  - open and close hour in agenda forms
  [nse]

## [0.0.41] - 02-07-2021 -
### Added
  - category iMio - ... and move forms into
  [nse]

## [0.0.40] - 01-07-2021 -
### Patched
  - 2 forms agenda
  [nse]

## [0.0.39] - 01-07-2021 -
### Patched
  - Changelog
  [nse]

## [0.0.38] - 01-07-2021 -
### Patched
  - bloc de champs personne for forms agenda
  [nse]

## [0.0.37] - 01-07-2021 -
### Added
  - workflow for forms agenda
  - froms agenda
  - category iMio - agenda
  - bloc de champs personne for forms agenda
  [nse]

## [0.0.36] - 01-07-2021 -
### Updated
  - workflow par défaut and herit
  [nse]

## [0.0.35] - 01-07-2021 -
### Added
  - modele date et heure
  - datasourec heure et minute
  [nse]

## [0.0.21] - 30-06-2021 -
### Delete
  - many forms for test
  [nse]

## [0.0.20] - 28-06-2021 -
### Update
  - blocs de champs
  [nse]


## [0.0.19] - 25-06-2021 -
### Added
  - mails template for wf par defaut
### Update
  - wf par defaut comment alert
  - blocs de champs
  [nse]


## [0.0.18] - 24-06-2021 -
### Added
  - Many blocs de champs
  - Many forms
  [nse]

## [0.0.17] - 23-06-2021 -
### Update
  - rename repo of blocs de champs V2
  [nse]

## [0.0.16] - 23-06-2021 -
### Update
  - rename repo of blocs de champs
  [nse]

## [0.0.15] - 23-06-2021 -
### Update
  - workflow bea chien dangereux
  [nse]

## [0.0.14] - 23-06-2021 -
### Update
  - workflow changement d'adresse V2
  [nse]


## [0.0.13] - 23-06-2021 -
### Update
  - workflow changement d'adresse
  [nse]

## [0.0.12] - 23-06-2021 -
### Update
  - all workflows v2
  [nse]

## [0.0.11] - 23-06-2021 -
### Update
  - all workflows
### Delete
  - all forms
  [nse]

## [0.0.10] - 22-06-2021 -
### Added
  - add many workflows V2
  [nse]


## [0.0.9] - 22-06-2021 -
### Added
  - add many workflows
  - add directory blockdef
  [nse]

## [0.0.8] - 21-06-2021 -
### Added
  - remove theaters mail-templates
  - rename categories as category
  [nhi]

## [0.0.7] - 21-06-2021 -
### Added
  - add pays datasource
  [nhi]

## [0.0.6] - 21-06-2021 -
### Added
  - add mail-templates
  - fix deployment path
  [nhi]

## [0.0.5] - 21-06-2021 -
### Added
  - add some files to test indus
  [nhi]

## [0.0.4] - 17-06-2021 -
### Added
  - add init.py
  - add random form to test
  [nhi]

## [0.0.3] - 17-06-2021 -
### Added
  - update version
  - clarify authors
  - add debian folder
  [nhi]

## [0.0.2] - 15-06-2021 -
### Added
  - adapt Jenkinsfile
  [nhi]
### Removed
  - old files
  [nhi]

## [0.0.1] - 15-04-2021 -
### Added
  - all files that where in the 'script-teleservices'
    and that will potentially be useful in this one.
  [dmu]
