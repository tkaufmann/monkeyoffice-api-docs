## Debitoren

[]{#debitoren_Datenstrukturen .anchor}

### Datenstrukturen von Debitoren

[]{#Parameter_DebitorenRechnungArt .anchor}

::: jsonproto
[DebitorenRechnungArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| { [\"DebitorenRechnungArt\"]{.jsonkey tag="DebitorenRechnungArt"}: [\...]{.jsonvalue} } |   ----------------------------------- ------------------------------------------------ |
|                                                                                         |   Aufzählung, Integer                 0=[DebitorRechnung]{tag="DebitorRechnung"}\      |
|                                                                                         |                                       1=[DebitorGutschrift]{tag="DebitorGutschrift"}   |
|                                                                                         |                                                                                        |
|                                                                                         |   ----------------------------------- ------------------------------------------------ |
+-----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenRechnungArtAnzeige .anchor}

::: jsonproto
[DebitorenRechnungArtAnzeige]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| { [\"DebitorenRechnungArtAnzeige\"]{.jsonkey tag="DebitorenRechnungArtAnzeige"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------- |
|                                                                                                       |   Aufzählung, Integer                 0=[Alle]{tag="Alle"}\                  |
|                                                                                                       |                                       1=[Rechnungen]{tag="Rechnungen"}\      |
|                                                                                                       |                                       2=[Gutschriften]{tag="Gutschriften"}   |
|                                                                                                       |                                                                              |
|                                                                                                       |   ----------------------------------- -------------------------------------- |
+-------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenbelegStatus .anchor}

::: jsonproto
[DebitorenbelegStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| { [\"DebitorenbelegStatus\"]{.jsonkey tag="DebitorenbelegStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------------------- |
|                                                                                         |   Aufzählung, Integer                 1=[Alle]{tag="Alle"}\                                    |
|                                                                                         |                                       2=[Nur Dokumente]{tag="Nur Dokumente"}\                  |
|                                                                                         |                                       3=[Nur Entwürfe/Vorlagen]{tag="Nur Entwürfe/Vorlagen"}   |
|                                                                                         |                                                                                                |
|                                                                                         |   ----------------------------------- -------------------------------------------------------- |
+-----------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenRechnungKalkbasis .anchor}

::: jsonproto
[DebitorenRechnungKalkbasis]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"DebitorenRechnungKalkbasis\"]{.jsonkey tag="DebitorenRechnungKalkbasis"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                                     |   Aufzählung, Integer                 0=[Netto]{tag="Netto"}\             |
|                                                                                                     |                                       1=[Brutto]{tag="Brutto"}            |
|                                                                                                     |                                                                           |
|                                                                                                     |   ----------------------------------- ----------------------------------- |
+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenRechnungListItem .anchor}

::: jsonproto
[DebitorenRechnungListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                      |
|                                                                                                                                        |
|   --------------------------------------------------------- -------------------------------------------------------------------------- |
|     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                                     |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                     |
|     [\"RechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},        [DebitorenRechnungArt](#Parameter_DebitorenRechnungArt){.navlinkcomment}   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        date (yyyy-mm-dd)                                                          |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                     |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                                     |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string, neu ab Version 20.0                                                |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                     |
|     [\"Brutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                     |
|     [\"Bezahlt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                     |
|     [\"Offen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                     |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                     |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}     string                                                                     |
|   --------------------------------------------------------- -------------------------------------------------------------------------- |
|                                                                                                                                        |
| }                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenRechnungItem .anchor}

::: jsonproto
[DebitorenRechnungItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                           |
|   ---------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------- |
|     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                       string                                                                                                     |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                      string                                                                                                     |
|     [\"RechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},                                                                           [DebitorenRechnungArt](#Parameter_DebitorenRechnungArt){.navlinkcomment}                                   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           date (yyyy-mm-dd)                                                                                          |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                         string                                                                                                     |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                            string                                                                                                     |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                        string, neu ab Version 20.0                                                                                |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           string                                                                                                     |
|     [\"Brutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                          string                                                                                                     |
|     [\"Bezahlt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                         string                                                                                                     |
|     [\"Offen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           string                                                                                                     |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                      string                                                                                                     |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                       string                                                                                                     |
|     [\"Entwurf\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                             boolean (true\|false)                                                                                      |
|     [\"Zahlungsbedingung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                                     |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                         [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}                                                     |
|     [\"TageNetto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                           integer                                                                                                    |
|     [\"TageSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                          integer                                                                                                    |
|     [\"ProzentSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                       float (0.0)                                                                                                |
|     [\"NichtMahnen\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                         boolean (true\|false)                                                                                      |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                   [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}                                         |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                        string                                                                                                     |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                            string                                                                                                     |
|     [\"AttachmentIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},                                                                Array vom Typ string                                                                                       |
|     [\"DebitorenRechnungPositionItemList\"]{.jsonkey}: [ { \"DebitorenRechnungPositionItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [DebitorenRechnungPositionItem](#Parameter_DebitorenRechnungPositionItem){.navlinkcomment}   |
|   ---------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                           |
| }                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenRechnungPositionItem .anchor}

::: jsonproto
[DebitorenRechnungPositionItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                        |
|                                                                                                                                          |
|   --------------------------------------------------------------------------- ---------------------------------------------------------- |
|     [\"Position\"]{.jsonkey}: [ \... ]{.jsonvalue},                           integer                                                    |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                     |
|     [\"BetragBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                 string                                                     |
|     [\"BetragBruttoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                 string                                                     |
|     [\"BetragNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                     |
|     [\"BetragNettoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                     |
|     [\"BetragSteuerFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                 string                                                     |
|     [\"BetragSteuerSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                 string                                                     |
|     [\"Ertragskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                       integer                                                    |
|     [\"Kostenstelle1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                     |
|     [\"Kostenstelle2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                     |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                     |
|     [\"OSS_Daten\"]{.jsonkey}: [ { \"OSSDatenItem\": {\...} } ]{.jsonvalue}   [OSSDatenItem](#Parameter_OSSDatenItem){.navlinkcomment}   |
|   --------------------------------------------------------------------------- ---------------------------------------------------------- |
|                                                                                                                                          |
| }                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenRechnungAddItem .anchor}

::: jsonproto
[DebitorenRechnungAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
|   ------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------- |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                         string                                                                                                           |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                              string                                                                                                           |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                              date (yyyy-mm-dd)                                                                                                |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                            string                                                                                                           |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                               string                                                                                                           |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           string                                                                                                           |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                         string                                                                                                           |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           string                                                                                                           |
|     [\"BerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},                                                                            [DebitorenRechnungKalkbasis](#Parameter_DebitorenRechnungKalkbasis){.navlinkcomment}                             |
|     [\"Zahlungsbedingung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                  string                                                                                                           |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                            [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}                                                           |
|     [\"TageNetto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                              integer                                                                                                          |
|     [\"TageSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                             integer                                                                                                          |
|     [\"ProzentSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                          float (0.0)                                                                                                      |
|     [\"NichtMahnen\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                            boolean (true\|false)                                                                                            |
|     [\"DebitorenRechnungPositionItemList\"]{.jsonkey}: [ { \"DebitorenRechnungPositionAddItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [DebitorenRechnungPositionAddItem](#Parameter_DebitorenRechnungPositionAddItem){.navlinkcomment}   |
|   ------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                                    |
| }                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenRechnungPositionAddItem .anchor}

::: jsonproto
[DebitorenRechnungPositionAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                |
|                                                                                                                                                  |
|   --------------------------------------------------------------------------- ------------------------------------------------------------------ |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string, neu ab Version 20.1.0, wirkt nur bei mehreren Positionen   |
|     [\"BetragBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                 string                                                             |
|     [\"BetragNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                             |
|     [\"Ertragskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                       integer                                                            |
|     [\"Kostenstelle1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                             |
|     [\"Kostenstelle2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                             |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                             |
|     [\"OSS_Daten\"]{.jsonkey}: [ { \"OSSDatenItem\": {\...} } ]{.jsonvalue}   [OSSDatenItem](#Parameter_OSSDatenItem){.navlinkcomment}           |
|   --------------------------------------------------------------------------- ------------------------------------------------------------------ |
|                                                                                                                                                  |
| }                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenRechnungFilter .anchor}

::: jsonproto
[DebitorenRechnungFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                         |
|                                                                                                                                                           |
|   -------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                                   |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          date (yyyy-mm-dd)                                                                        |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          date (yyyy-mm-dd)                                                                        |
|     [\"Rechnungsart\"]{.jsonkey}: [\...]{.jsonvalue},            [DebitorenRechnungArtAnzeige](#Parameter_DebitorenRechnungArtAnzeige){.navlinkcomment}   |
|     [\"RechnungsNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                                   |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                                   |
|     [\"Debitorenkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                                                  |
|     [\"Erfolgskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},          integer                                                                                  |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                                   |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},     [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}                       |
|     [\"DebitorenbelegStatus\"]{.jsonkey}: [ \... ]{.jsonvalue}   [DebitorenbelegStatus](#Parameter_DebitorenbelegStatus){.navlinkcomment}                 |
|   -------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
|                                                                                                                                                           |
| }                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenZahlungListItem .anchor}

::: jsonproto
[DebitorenZahlungListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------+
| {                                                                               |
|                                                                                 |
|   --------------------------------------------------------- ------------------- |
|     [\"Zahlung_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string              |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string              |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        date (yyyy-mm-dd)   |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string              |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string              |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string              |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string              |
|     [\"Zahlung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string              |
|     [\"Minderung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}     string              |
|   --------------------------------------------------------- ------------------- |
|                                                                                 |
| }                                                                               |
+---------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenZahlungItem .anchor}

::: jsonproto
[DebitorenZahlungItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                     |
|                                                                                                                       |
|   ---------------------------------------------------------- -------------------------------------------------------- |
|     [\"Zahlung_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                   |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         date (yyyy-mm-dd)                                        |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                   |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                   |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                   |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                   |
|     [\"Zahlung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                   |
|     [\"Minderung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                   |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue},       [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}   |
|     [\"D-Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                   |
|     [\"ZahlungSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                   |
|     [\"MinderungSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                   |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                   |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}       string                                                   |
|   ---------------------------------------------------------- -------------------------------------------------------- |
|                                                                                                                       |
| }                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DebitorenZahlungFilter .anchor}

::: jsonproto
[DebitorenZahlungFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------+
| {                                                                                |
|                                                                                  |
|   ---------------------------------------------------------- ------------------- |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string              |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      date (yyyy-mm-dd)   |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      date (yyyy-mm-dd)   |
|     [\"RechnungsNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string              |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string              |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}       string              |
|   ---------------------------------------------------------- ------------------- |
|                                                                                  |
| }                                                                                |
+----------------------------------------------------------------------------------+
:::

\
[]{#debitoren .anchor}\

### Funktionsliste von Debitoren

[]{#debitoren_debitorenRechnungFilterTemplate .anchor}

::::: memitem
::: memproto
[debitorenRechnungFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Filter Debitorenrechnungen

**Aufruf:**
:   { \"debitorenRechnungFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"debitorenRechnungFilterTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                          |
    |   --------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DebitorenRechnungFilter\": {\...} } ]{.jsonvalue}   [DebitorenRechnungFilter](#Parameter_DebitorenRechnungFilter){.navlinkcomment}   |
    |   --------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
    |                                                                                                                                                                            |
    | }                                                                                                                                                                          |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenRechnungList .anchor}

::::: memitem
::: memproto
[debitorenRechnungList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung Debitorenrechnungen

**Aufruf:**
:   { \"debitorenRechnungList\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                               |
    |   ----------------------------------------------------------------- ------------------------------------------------------------------------------------------- |
    |     [\"DebitorenRechnungFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [DebitorenRechnungFilter](#Parameter_DebitorenRechnungFilter){.navlinkcomment} (optional)   |
    |   ----------------------------------------------------------------- ------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                 |
    | }                                                                                                                                                               |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenRechnungListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                      |
    |   ------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DebitorenRechnungListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [DebitorenRechnungListItem](#Parameter_DebitorenRechnungListItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                        |
    | }                                                                                                                                                                                                      |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenRechnungGet .anchor}

::::: memitem
::: memproto
[debitorenRechnungGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details einer Debitorenrechnung

**Aufruf:**
:   { \"debitorenRechnungGet\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   ------------------------------------------------------- --------    |
    |     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string      |
    |   ------------------------------------------------------- --------    |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenRechnungGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                    |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DebitorenRechnungItem\": {\...} } ]{.jsonvalue}   [DebitorenRechnungItem](#Parameter_DebitorenRechnungItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |                                                                                                                                                                      |
    | }                                                                                                                                                                    |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenRechnungTemplate .anchor}

::::: memitem
::: memproto
[debitorenRechnungTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert DebitorenRechnungAddItem als Vorlage

**Aufruf:**
:   { \"debitorenRechnungTemplate\":
    +---------------------------------------------------------------------------------------------+
    | {                                                                                           |
    |   ---------------------------------------------------------- ------------------------------ |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string (optional)              |
    |     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         date (yyyy-mm-dd) (optional)   |
    |     [\"PositionenAnzahl\"]{.jsonkey}: [ \... ]{.jsonvalue}   integer (optional)             |
    |   ---------------------------------------------------------- ------------------------------ |
    |                                                                                             |
    | }                                                                                           |
    +---------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenRechnungTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                             |
    |   ---------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DebitorenRechnungAddItem\": {\...} } ]{.jsonvalue}   [DebitorenRechnungAddItem](#Parameter_DebitorenRechnungAddItem){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------- |
    |                                                                                                                                                                               |
    | }                                                                                                                                                                             |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenRechnungPreview .anchor}

::::: memitem
::: memproto
[debitorenRechnungPreview]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
berechnet eine neue Debitorenrechnung, ohne speichern

**Aufruf:**
:   { \"debitorenRechnungPreview\":
    +---------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                       |
    |   ------------------------------------------------------------------ ---------------------------------------------------------------------------------- |
    |     [\"DebitorenRechnungAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [DebitorenRechnungAddItem](#Parameter_DebitorenRechnungAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------ ---------------------------------------------------------------------------------- |
    |                                                                                                                                                         |
    | }                                                                                                                                                       |
    +---------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenRechnungPreviewResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                    |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DebitorenRechnungItem\": {\...} } ]{.jsonvalue}   [DebitorenRechnungItem](#Parameter_DebitorenRechnungItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |                                                                                                                                                                      |
    | }                                                                                                                                                                    |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenRechnungAdd .anchor}

::::: memitem
::: memproto
[debitorenRechnungAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt eine neue Debitorenrechnung hinzu

**Aufruf:**
:   { \"debitorenRechnungAdd\":
    +---------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                       |
    |   ------------------------------------------------------------------ ---------------------------------------------------------------------------------- |
    |     [\"DebitorenRechnungAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [DebitorenRechnungAddItem](#Parameter_DebitorenRechnungAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------ ---------------------------------------------------------------------------------- |
    |                                                                                                                                                         |
    | }                                                                                                                                                       |
    +---------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenRechnungAddResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenRechnungDelete .anchor}

::::: memitem
::: memproto
[debitorenRechnungDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht eine vorhandene Debitorenrechnung

**Aufruf:**
:   { \"debitorenRechnungDelete\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   ------------------------------------------------------- --------    |
    |     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string      |
    |   ------------------------------------------------------- --------    |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenRechnungDeleteResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenRechnungAddAttachment .anchor}

::::: memitem
::: memproto
[debitorenRechnungAddAttachment]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt ein Attachment einer Debitorenrechnung hinzu

**Aufruf:**
:   { \"debitorenRechnungAddAttachment\":
    +------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                  |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                               |
    |     [\"AttachmentAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AttachmentAddItem](#Parameter_AttachmentAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                    |
    | }                                                                                                                                  |
    +------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenRechnungAddAttachmentResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenZahlungFilterTemplate .anchor}

::::: memitem
::: memproto
[debitorenZahlungFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Filter Debitorenzahlungen

**Aufruf:**
:   { \"debitorenZahlungFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"debitorenZahlungFilterTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DebitorenZahlungFilter\": {\...} } ]{.jsonvalue}   [DebitorenZahlungFilter](#Parameter_DebitorenZahlungFilter){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |                                                                                                                                                                         |
    | }                                                                                                                                                                       |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenZahlungList .anchor}

::::: memitem
::: memproto
[debitorenZahlungList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung Debitorenzahlungen

**Aufruf:**
:   { \"debitorenZahlungList\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                            |
    |   ---------------------------------------------------------------- ----------------------------------------------------------------------------------------- |
    |     [\"DebitorenZahlungFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [DebitorenZahlungFilter](#Parameter_DebitorenZahlungFilter){.navlinkcomment} (optional)   |
    |   ---------------------------------------------------------------- ----------------------------------------------------------------------------------------- |
    |                                                                                                                                                              |
    | }                                                                                                                                                            |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenZahlungListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                   |
    |   ------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DebitorenZahlungListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [DebitorenZahlungListItem](#Parameter_DebitorenZahlungListItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------ |
    |                                                                                                                                                                                                     |
    | }                                                                                                                                                                                                   |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenZahlungGet .anchor}

::::: memitem
::: memproto
[debitorenZahlungGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details einer Debitorenzahlung

**Aufruf:**
:   { \"debitorenZahlungGet\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Zahlung_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenZahlungGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                 |
    |   ------------------------------------------------------------------------------------ -------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DebitorenZahlungItem\": {\...} } ]{.jsonvalue}   [DebitorenZahlungItem](#Parameter_DebitorenZahlungItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------ -------------------------------------------------------------------------- |
    |                                                                                                                                                                   |
    | }                                                                                                                                                                 |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#debitoren_debitorenZahlungCreate .anchor}

:::::: memitem
::: memproto
[debitorenZahlungCreate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
erzeugt Zahlung für Debitorenrechnung

::: mohelpinfo
\
Es wird für einen vorhandenen Debitoren-Rechnung eine Zahlung angelegt.\
Ablauf:\
1. Posten_ID ermitteln für welchen eine Zahlung angelegt werden soll( z.B. über debitorenRechnungList).\
2. Funktion debitorenZahlungCreate mit Parameter Posten_ID,Datum,Konto,Zahlungsart ausführen.\
Es wird eine Zahlung angelegt, Rückgabe InsertID oder Fehlerstatus.
:::

**Aufruf:**
:   { \"debitorenZahlungCreate\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   -------------------------------------------------------- ------------------------------------------------------------------------------------------------ |
    |     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                                           |
    |     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       date (yyyy-mm-dd)                                                                                |
    |     [\"Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},           integer                                                                                          |
    |     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue}      [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}, optional, default ist Angabe im Posten   |
    |   -------------------------------------------------------- ------------------------------------------------------------------------------------------------ |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenZahlungCreateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#debitoren_debitorenZahlungDelete .anchor}

::::: memitem
::: memproto
[debitorenZahlungDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht eine vorhandene Debitorenzahlung

**Aufruf:**
:   { \"debitorenZahlungDelete\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Zahlung_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"debitorenZahlungDeleteResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ReturnStatus\": {\...} } ]{.jsonvalue}   [ReturnStatus](#Parameter_ReturnStatus){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#Content_kreditoren .anchor}  \

