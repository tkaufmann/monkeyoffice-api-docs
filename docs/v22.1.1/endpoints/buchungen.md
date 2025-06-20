## Buchungen

[]{#buchungen_Datenstrukturen .anchor}

### Datenstrukturen von Buchungen

[]{#Parameter_BuchungStatus .anchor}

::: jsonproto
[BuchungStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| { [\"BuchungStatus\"]{.jsonkey tag="BuchungStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------------------------- |
|                                                                           |   Aufzählung, Integer                 1=[Nicht festgeschrieben]{tag="Nicht festgeschrieben"}\   |
|                                                                           |                                       2=[Festgeschrieben]{tag="Festgeschrieben"}\               |
|                                                                           |                                       4=[Alle]{tag="Alle"}                                      |
|                                                                           |                                                                                                 |
|                                                                           |   ----------------------------------- --------------------------------------------------------- |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_BuchungFilter .anchor}

::: jsonproto
[BuchungFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                   |
|                                                                                                                                     |
|   ------------------------------------------------------------ -------------------------------------------------------------------- |
|     [\"Suchtext\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                               |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        date (yyyy-mm-dd)                                                    |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        date (yyyy-mm-dd)                                                    |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},   [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}   |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                               |
|     [\"Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},               integer                                                              |
|     [\"KontoSoll\"]{.jsonkey}: [ \... ]{.jsonvalue},           integer                                                              |
|     [\"KontoHaben\"]{.jsonkey}: [ \... ]{.jsonvalue}           integer                                                              |
|   ------------------------------------------------------------ -------------------------------------------------------------------- |
|                                                                                                                                     |
| }                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_BuchungListItem .anchor}

::: jsonproto
[BuchungListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                       |
|                                                                                                                                                         |
|   --------------------------------------------------------- ------------------------------------------------------------------------------------------- |
|     [\"Buchung_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                                      |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                                      |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                                                      |
|     [\"Status\"]{.jsonkey}: [\...]{.jsonvalue},             [BuchungStatus](#Parameter_BuchungStatus){.navlinkcomment}, veraltet, nicht mehr benutzen   |
|     [\"Summe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                                      |
|     [\"SummeFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                                      |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}       string                                                                                      |
|   --------------------------------------------------------- ------------------------------------------------------------------------------------------- |
|                                                                                                                                                         |
| }                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_BuchungItem .anchor}

::: jsonproto
[BuchungItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                       |
|   ------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------- |
|     [\"Buchung_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                 string                                                                                                      |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                      string                                                                                                      |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string                                                                                                      |
|     [\"Status\"]{.jsonkey}: [\...]{.jsonvalue},                                                           [BuchungStatus](#Parameter_BuchungStatus){.navlinkcomment}, veraltet, nicht mehr benutzen                   |
|     [\"Summe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                      string                                                                                                      |
|     [\"SummeFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                    string                                                                                                      |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                    string                                                                                                      |
|     [\"EingabeDatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                               string                                                                                                      |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                   string                                                                                                      |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                    string                                                                                                      |
|     [\"KontoSoll\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                      integer                                                                                                     |
|     [\"KontoHaben\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                     integer                                                                                                     |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                   string                                                                                                      |
|     [\"Kurs\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string                                                                                                      |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                 string                                                                                                      |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},                                              [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}                                          |
|     [\"BuchungJournalItemList\"]{.jsonkey}: [ { \"BuchungJournalItem\": \[ {}, \... \] } ]{.jsonvalue},   Array vom Typ [BuchungJournalItem](#Parameter_BuchungJournalItem){.navlinkcomment}, Neu ab Version 18.1.0   |
|     [\"AttachmentIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue}                                            Array vom Typ string, readonly                                                                              |
|   ------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                       |
| }                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_BuchungAddItem .anchor}

::: jsonproto
[BuchungAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                          |
|                                                                                                                                                                                                            |
|   ----------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------- |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                          string                                                                                       |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           string                                                                                       |
|     [\"BelegNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string                                                                                       |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string                                                                                       |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string                                                                                       |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string                                                                                       |
|     [\"Kurs\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           string                                                                                       |
|     [\"BuchungPositionItemList\"]{.jsonkey}: [ { \"BuchungPositionAddItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [BuchungPositionAddItem](#Parameter_BuchungPositionAddItem){.navlinkcomment}   |
|   ----------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                            |
| }                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_BuchungPositionAddItem .anchor}

::: jsonproto
[BuchungPositionAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                        |
|                                                                                                                                          |
|   --------------------------------------------------------------------------- ---------------------------------------------------------- |
|     [\"Betrag\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                     |
|     [\"KontoSoll\"]{.jsonkey}: [ \... ]{.jsonvalue},                          integer                                                    |
|     [\"KontoHaben\"]{.jsonkey}: [ \... ]{.jsonvalue},                         integer                                                    |
|     [\"Kostenstelle1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                     |
|     [\"Kostenstelle2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                     |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                     |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                     |
|     [\"BuchungBetragBasis\"]{.jsonkey}: [ \... ]{.jsonvalue},                 integer, derzeit nicht in Benutzung                        |
|     [\"OSS_Daten\"]{.jsonkey}: [ { \"OSSDatenItem\": {\...} } ]{.jsonvalue}   [OSSDatenItem](#Parameter_OSSDatenItem){.navlinkcomment}   |
|   --------------------------------------------------------------------------- ---------------------------------------------------------- |
|                                                                                                                                          |
| }                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_BuchungJournalItem .anchor}

::: jsonproto
[BuchungJournalItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: jsondoc
::: mohelpinfo
Neu ab Version 18.1.0
:::

+------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                        |
|                                                                                                                                          |
|   --------------------------------------------------------------------------- ---------------------------------------------------------- |
|     [\"Journalnummer\"]{.jsonkey}: [ \... ]{.jsonvalue},                      integer                                                    |
|     [\"Konto\"]{.jsonkey}: [ \... ]{.jsonvalue},                              integer                                                    |
|     [\"Kontobezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},               string                                                     |
|     [\"BetragSoll\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                     |
|     [\"BetragHaben\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                    string                                                     |
|     [\"Steuersatz\"]{.jsonkey}: [ \... ]{.jsonvalue},                         integer                                                    |
|     [\"Text\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                           string                                                     |
|     [\"Kostenstelle1\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                     |
|     [\"Kostenstelle2\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                     |
|     [\"FW_Soll\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                     |
|     [\"FW_Haben\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                       string                                                     |
|     [\"OSS_Daten\"]{.jsonkey}: [ { \"OSSDatenItem\": {\...} } ]{.jsonvalue}   [OSSDatenItem](#Parameter_OSSDatenItem){.navlinkcomment}   |
|   --------------------------------------------------------------------------- ---------------------------------------------------------- |
|                                                                                                                                          |
| }                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------+
::::

\
[]{#buchungen .anchor}\

### Funktionsliste von Buchungen

[]{#buchungen_buchungFilterTemplate .anchor}

::::: memitem
::: memproto
[buchungFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Buchung-Filter

**Aufruf:**
:   { \"buchungFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"buchungFilterTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                            |
    |   ----------------------------------------------------------------------------- ------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"BuchungFilter\": {\...} } ]{.jsonvalue}   [BuchungFilter](#Parameter_BuchungFilter){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------- ------------------------------------------------------------ |
    |                                                                                                                                              |
    | }                                                                                                                                            |
    +----------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#buchungen_buchungList .anchor}

::::: memitem
::: memproto
[buchungList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Listet alle Buchungen

**Aufruf:**
:   { \"buchungList\":
    +-----------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                 |
    |   ------------------------------------------------------- ----------------------------------------------------------------------- |
    |     [\"BuchungFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [BuchungFilter](#Parameter_BuchungFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------- ----------------------------------------------------------------------- |
    |                                                                                                                                   |
    | }                                                                                                                                 |
    +-----------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"buchungListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                        |
    |   --------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"BuchungListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [BuchungListItem](#Parameter_BuchungListItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |                                                                                                                                                                          |
    | }                                                                                                                                                                        |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#buchungen_buchungGet .anchor}

::::: memitem
::: memproto
[buchungGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Eigenschaften einer Buchung

**Aufruf:**
:   { \"buchungGet\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Buchung_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"buchungGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                      |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"BuchungItem\": {\...} } ]{.jsonvalue}   [BuchungItem](#Parameter_BuchungItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |                                                                                                                                        |
    | }                                                                                                                                      |
    +----------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#buchungen_buchungTemplate .anchor}

::::: memitem
::: memproto
[buchungTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert BuchungAddItem als Vorlage

**Aufruf:**
:   { \"buchungTemplate\":
    +-----------------------------------------------------------------------------------+
    | {                                                                                 |
    |   ---------------------------------------------------------- -------------------- |
    |     [\"PositionenAnzahl\"]{.jsonkey}: [ \... ]{.jsonvalue}   integer (optional)   |
    |   ---------------------------------------------------------- -------------------- |
    |                                                                                   |
    | }                                                                                 |
    +-----------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"buchungTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                               |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"BuchungAddItem\": {\...} } ]{.jsonvalue}   [BuchungAddItem](#Parameter_BuchungAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |                                                                                                                                                 |
    | }                                                                                                                                               |
    +-------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#buchungen_buchungAdd .anchor}

:::::: memitem
::: memproto
[buchungAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
fügt neue Buchung hinzu

::: mohelpinfo
\
Hinweis: Standardbuchungen enthalten ein BuchungPositionAddItem\
Mehrere BuchungPositionAddItem werden für Splitt-Buchungen verwendet
:::

**Aufruf:**
:   { \"buchungAdd\":
    +---------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                         |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |     [\"BuchungAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [BuchungAddItem](#Parameter_BuchungAddItem){.navlinkcomment}   |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |                                                                                                                           |
    | }                                                                                                                         |
    +---------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"buchungAddResponse\":
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

[]{#buchungen_buchungAddAttachment .anchor}

::::: memitem
::: memproto
[buchungAddAttachment]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt ein Attachment einer Buchung hinzu

**Aufruf:**
:   { \"buchungAddAttachment\":
    +------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                  |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"Buchung_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                               |
    |     [\"AttachmentAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AttachmentAddItem](#Parameter_AttachmentAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                    |
    | }                                                                                                                                  |
    +------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"buchungAddAttachmentResponse\":
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

[]{#Content_debitoren .anchor}  \

