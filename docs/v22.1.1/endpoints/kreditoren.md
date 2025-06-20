## Kreditoren

[]{#kreditoren_Datenstrukturen .anchor}

### Datenstrukturen von Kreditoren

[]{#Parameter_KreditorenRechnungArt .anchor}

::: jsonproto
[KreditorenRechnungArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| { [\"KreditorenRechnungArt\"]{.jsonkey tag="KreditorenRechnungArt"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------------- |
|                                                                                           |   Aufzählung, Integer                 2=[KreditorRechnung]{tag="KreditorRechnung"}\      |
|                                                                                           |                                       3=[KreditorGutschrift]{tag="KreditorGutschrift"}   |
|                                                                                           |                                                                                          |
|                                                                                           |   ----------------------------------- -------------------------------------------------- |
+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenRechnungArtAnzeige .anchor}

::: jsonproto
[KreditorenRechnungArtAnzeige]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| { [\"KreditorenRechnungArtAnzeige\"]{.jsonkey tag="KreditorenRechnungArtAnzeige"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------- |
|                                                                                                         |   Aufzählung, Integer                 0=[Alle]{tag="Alle"}\                  |
|                                                                                                         |                                       1=[Rechnungen]{tag="Rechnungen"}\      |
|                                                                                                         |                                       2=[Gutschriften]{tag="Gutschriften"}   |
|                                                                                                         |                                                                              |
|                                                                                                         |   ----------------------------------- -------------------------------------- |
+---------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenRechnungKalkbasis .anchor}

::: jsonproto
[KreditorenRechnungKalkbasis]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"KreditorenRechnungKalkbasis\"]{.jsonkey tag="KreditorenRechnungKalkbasis"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                                       |   Aufzählung, Integer                 0=[Netto]{tag="Netto"}\             |
|                                                                                                       |                                       1=[Brutto]{tag="Brutto"}            |
|                                                                                                       |                                                                           |
|                                                                                                       |   ----------------------------------- ----------------------------------- |
+-------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenRechnungListItem .anchor}

::: jsonproto
[KreditorenRechnungListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                        |
|                                                                                                                                          |
|   --------------------------------------------------------- ---------------------------------------------------------------------------- |
|     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                                       |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                       |
|     [\"RechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},        [KreditorenRechnungArt](#Parameter_KreditorenRechnungArt){.navlinkcomment}   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        date (yyyy-mm-dd)                                                            |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                       |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                                       |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string, neu ab Version 20.0                                                  |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                       |
|     [\"Brutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                       |
|     [\"Bezahlt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                       |
|     [\"Offen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                       |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                       |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}     string                                                                       |
|   --------------------------------------------------------- ---------------------------------------------------------------------------- |
|                                                                                                                                          |
| }                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenRechnungItem .anchor}

::: jsonproto
[KreditorenRechnungItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                               |
|   ------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------ |
|     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                         string                                                                                                       |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                        string                                                                                                       |
|     [\"RechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},                                                                             [KreditorenRechnungArt](#Parameter_KreditorenRechnungArt){.navlinkcomment}                                   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                             date (yyyy-mm-dd)                                                                                            |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           string                                                                                                       |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                              string                                                                                                       |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                          string, neu ab Version 20.0                                                                                  |
|     [\"Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                             string                                                                                                       |
|     [\"Brutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                            string                                                                                                       |
|     [\"Bezahlt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           string                                                                                                       |
|     [\"Offen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                             string                                                                                                       |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                        string                                                                                                       |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                         string                                                                                                       |
|     [\"Entwurf\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                               boolean (true\|false)                                                                                        |
|     [\"Zahlungsbedingung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string                                                                                                       |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                           [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}                                                       |
|     [\"TageNetto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                             integer                                                                                                      |
|     [\"TageSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                            integer                                                                                                      |
|     [\"ProzentSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                         float (0.0)                                                                                                  |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                     [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}                                           |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                          string                                                                                                       |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                              string                                                                                                       |
|     [\"AttachmentIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},                                                                  Array vom Typ string                                                                                         |
|     [\"KreditorenRechnungPositionItemList\"]{.jsonkey}: [ { \"KreditorenRechnungPositionItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [KreditorenRechnungPositionItem](#Parameter_KreditorenRechnungPositionItem){.navlinkcomment}   |
|   ------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                                                                                                               |
| }                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenRechnungPositionItem .anchor}

::: jsonproto
[KreditorenRechnungPositionItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+
| {                                                                         |
|                                                                           |
|   ------------------------------------------------------------- --------- |
|     [\"Position\"]{.jsonkey}: [ \... ]{.jsonvalue},             integer   |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string    |
|     [\"BetragBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"BetragBruttoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"BetragNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"BetragNettoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"BetragSteuerFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"BetragSteuerSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
|     [\"Aufwandskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer   |
|     [\"Kostenstelle1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"Kostenstelle2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string    |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}        string    |
|   ------------------------------------------------------------- --------- |
|                                                                           |
| }                                                                         |
+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenRechnungAddItem .anchor}

::: jsonproto
[KreditorenRechnungAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
|   --------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------ |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           string                                                                                                             |
|     [\"Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                                    integer                                                                                                            |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                                date (yyyy-mm-dd)                                                                                                  |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                              string                                                                                                             |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                                 string                                                                                                             |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                             string                                                                                                             |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                           string                                                                                                             |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                             string                                                                                                             |
|     [\"BerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},                                                                              [KreditorenRechnungKalkbasis](#Parameter_KreditorenRechnungKalkbasis){.navlinkcomment}                             |
|     [\"Zahlungsbedingung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                    string                                                                                                             |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                              [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}                                                             |
|     [\"TageNetto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                                integer                                                                                                            |
|     [\"TageSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                               integer                                                                                                            |
|     [\"ProzentSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                            float (0.0)                                                                                                        |
|     [\"KreditorenRechnungPositionItemList\"]{.jsonkey}: [ { \"KreditorenRechnungPositionAddItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [KreditorenRechnungPositionAddItem](#Parameter_KreditorenRechnungPositionAddItem){.navlinkcomment}   |
|   --------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                                                                                                                        |
| }                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenRechnungPositionAddItem .anchor}

::: jsonproto
[KreditorenRechnungPositionAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                  |
|                                                                                                                                    |
|   ------------------------------------------------------------- ------------------------------------------------------------------ |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string, neu ab Version 20.1.0, wirkt nur bei mehreren Positionen   |
|     [\"BetragBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                             |
|     [\"BetragNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                             |
|     [\"Aufwandskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                            |
|     [\"Kostenstelle1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                             |
|     [\"Kostenstelle2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                             |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}        string                                                             |
|   ------------------------------------------------------------- ------------------------------------------------------------------ |
|                                                                                                                                    |
| }                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenRechnungFilter .anchor}

::: jsonproto
[KreditorenRechnungFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                            |
|                                                                                                                                                              |
|   --------------------------------------------------------------- ------------------------------------------------------------------------------------------ |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                                                     |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           date (yyyy-mm-dd)                                                                          |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           date (yyyy-mm-dd)                                                                          |
|     [\"Rechnungsart\"]{.jsonkey}: [\...]{.jsonvalue},             [KreditorenRechnungArtAnzeige](#Parameter_KreditorenRechnungArtAnzeige){.navlinkcomment}   |
|     [\"RechnungsNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                                     |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},               string                                                                                     |
|     [\"Kreditorenkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                                                    |
|     [\"Aufwandkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},           integer                                                                                    |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                                                     |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},      [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}                         |
|     [\"KreditorenbelegStatus\"]{.jsonkey}: [ \... ]{.jsonvalue}   [KreditorenbelegStatus](#Parameter_KreditorenbelegStatus){.navlinkcomment}                 |
|   --------------------------------------------------------------- ------------------------------------------------------------------------------------------ |
|                                                                                                                                                              |
| }                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KreditorenZahlungListItem .anchor}

::: jsonproto
[KreditorenZahlungListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
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
[]{#Parameter_KreditorenZahlungItem .anchor}

::: jsonproto
[KreditorenZahlungItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
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
|     [\"K-Konto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                   |
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
[]{#Parameter_KreditorenZahlungFilter .anchor}

::: jsonproto
[KreditorenZahlungFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
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
[]{#kreditoren .anchor}\

### Funktionsliste von Kreditoren

[]{#kreditoren_kreditorenRechnungFilterTemplate .anchor}

::::: memitem
::: memproto
[kreditorenRechnungFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Filter Kreditorenrechnungen

**Aufruf:**
:   { \"kreditorenRechnungFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"kreditorenRechnungFilterTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                             |
    |   ---------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KreditorenRechnungFilter\": {\...} } ]{.jsonvalue}   [KreditorenRechnungFilter](#Parameter_KreditorenRechnungFilter){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------- |
    |                                                                                                                                                                               |
    | }                                                                                                                                                                             |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#kreditoren_kreditorenRechnungList .anchor}

::::: memitem
::: memproto
[kreditorenRechnungList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung Kreditorenrechnungen

**Aufruf:**
:   { \"kreditorenRechnungList\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                  |
    |   ------------------------------------------------------------------ --------------------------------------------------------------------------------------------- |
    |     [\"KreditorenRechnungFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [KreditorenRechnungFilter](#Parameter_KreditorenRechnungFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------------------ --------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                    |
    | }                                                                                                                                                                  |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"kreditorenRechnungListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                         |
    |   -------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KreditorenRechnungListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [KreditorenRechnungListItem](#Parameter_KreditorenRechnungListItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                           |
    | }                                                                                                                                                                                                         |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#kreditoren_kreditorenRechnungGet .anchor}

::::: memitem
::: memproto
[kreditorenRechnungGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details einer Kreditorenrechnung

**Aufruf:**
:   { \"kreditorenRechnungGet\":
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
:   { \"kreditorenRechnungGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KreditorenRechnungItem\": {\...} } ]{.jsonvalue}   [KreditorenRechnungItem](#Parameter_KreditorenRechnungItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |                                                                                                                                                                         |
    | }                                                                                                                                                                       |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#kreditoren_kreditorenRechnungTemplate .anchor}

::::: memitem
::: memproto
[kreditorenRechnungTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert KreditorenRechnungAddItem als Vorlage

**Aufruf:**
:   { \"kreditorenRechnungTemplate\":
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
:   { \"kreditorenRechnungTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                |
    |   ----------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KreditorenRechnungAddItem\": {\...} } ]{.jsonvalue}   [KreditorenRechnungAddItem](#Parameter_KreditorenRechnungAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------ |
    |                                                                                                                                                                                  |
    | }                                                                                                                                                                                |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#kreditoren_kreditorenRechnungPreview .anchor}

::::: memitem
::: memproto
[kreditorenRechnungPreview]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
berechnet eine neue Kreditorenrechnung, ohne speichern

**Aufruf:**
:   { \"kreditorenRechnungPreview\":
    +------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                          |
    |   ------------------------------------------------------------------- ------------------------------------------------------------------------------------ |
    |     [\"KreditorenRechnungAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [KreditorenRechnungAddItem](#Parameter_KreditorenRechnungAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------- ------------------------------------------------------------------------------------ |
    |                                                                                                                                                            |
    | }                                                                                                                                                          |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"kreditorenRechnungPreviewResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KreditorenRechnungItem\": {\...} } ]{.jsonvalue}   [KreditorenRechnungItem](#Parameter_KreditorenRechnungItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |                                                                                                                                                                         |
    | }                                                                                                                                                                       |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#kreditoren_kreditorenRechnungAdd .anchor}

::::: memitem
::: memproto
[kreditorenRechnungAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt eine neue Kreditorenrechnung hinzu

**Aufruf:**
:   { \"kreditorenRechnungAdd\":
    +------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                          |
    |   ------------------------------------------------------------------- ------------------------------------------------------------------------------------ |
    |     [\"KreditorenRechnungAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [KreditorenRechnungAddItem](#Parameter_KreditorenRechnungAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------- ------------------------------------------------------------------------------------ |
    |                                                                                                                                                            |
    | }                                                                                                                                                          |
    +------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"kreditorenRechnungAddResponse\":
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

[]{#kreditoren_kreditorenRechnungDelete .anchor}

::::: memitem
::: memproto
[kreditorenRechnungDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht eine vorhandene Kreditorenrechnung

**Aufruf:**
:   { \"kreditorenRechnungDelete\":
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
:   { \"kreditorenRechnungDeleteResponse\":
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

[]{#kreditoren_kreditorenRechnungAddAttachment .anchor}

::::: memitem
::: memproto
[kreditorenRechnungAddAttachment]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt ein Attachment einer Kreditorenrechnung hinzu

**Aufruf:**
:   { \"kreditorenRechnungAddAttachment\":
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
:   { \"kreditorenRechnungAddAttachmentResponse\":
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

[]{#kreditoren_kreditorenZahlungFilterTemplate .anchor}

::::: memitem
::: memproto
[kreditorenZahlungFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Filter Kreditorenzahlungen

**Aufruf:**
:   { \"kreditorenZahlungFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"kreditorenZahlungFilterTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                          |
    |   --------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KreditorenZahlungFilter\": {\...} } ]{.jsonvalue}   [KreditorenZahlungFilter](#Parameter_KreditorenZahlungFilter){.navlinkcomment}   |
    |   --------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
    |                                                                                                                                                                            |
    | }                                                                                                                                                                          |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#kreditoren_kreditorenZahlungList .anchor}

::::: memitem
::: memproto
[kreditorenZahlungList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung Kreditorenzahlungen

**Aufruf:**
:   { \"kreditorenZahlungList\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                               |
    |   ----------------------------------------------------------------- ------------------------------------------------------------------------------------------- |
    |     [\"KreditorenZahlungFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [KreditorenZahlungFilter](#Parameter_KreditorenZahlungFilter){.navlinkcomment} (optional)   |
    |   ----------------------------------------------------------------- ------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                 |
    | }                                                                                                                                                               |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"kreditorenZahlungListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                      |
    |   ------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KreditorenZahlungListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [KreditorenZahlungListItem](#Parameter_KreditorenZahlungListItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                        |
    | }                                                                                                                                                                                                      |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#kreditoren_kreditorenZahlungGet .anchor}

::::: memitem
::: memproto
[kreditorenZahlungGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details einer Kreditorenzahlung

**Aufruf:**
:   { \"kreditorenZahlungGet\":
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
:   { \"kreditorenZahlungGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                    |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KreditorenZahlungItem\": {\...} } ]{.jsonvalue}   [KreditorenZahlungItem](#Parameter_KreditorenZahlungItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |                                                                                                                                                                      |
    | }                                                                                                                                                                    |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#kreditoren_kreditorenZahlungCreate .anchor}

:::::: memitem
::: memproto
[kreditorenZahlungCreate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
erzeugt Zahlung für Kreditorenrechnung

::: mohelpinfo
\
Es wird für eine vorhandenen Kreditoren-Rechnung eine Zahlung angelegt.\
Ablauf:\
1. Posten_ID ermitteln für welchen eine Zahlung angelegt werden soll( z.B. über kreditorenRechnungList).\
2. Funktion kreditorenZahlungCreate mit Parameter Posten_ID,Datum,Konto,Zahlungsart ausführen.\
Es wird eine Zahlung angelegt, Rückgabe InsertID oder Fehlerstatus.
:::

**Aufruf:**
:   { \"kreditorenZahlungCreate\":
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
:   { \"kreditorenZahlungCreateResponse\":
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

[]{#kreditoren_kreditorenZahlungDelete .anchor}

::::: memitem
::: memproto
[kreditorenZahlungDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht eine vorhandene Kreditorenzahlung

**Aufruf:**
:   { \"kreditorenZahlungDelete\":
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
:   { \"kreditorenZahlungDeleteResponse\":
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

[]{#Content_offenePosten .anchor}  \

