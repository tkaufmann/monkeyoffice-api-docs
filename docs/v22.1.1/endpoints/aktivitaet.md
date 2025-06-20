## Aktivitaet

::: mohelpinfo
\
Diese Modul erlaubt das Auflisten/Anlegen/Modifizieren und Löschen von Aktivitäten. Aktivitäten können mit Projekten bzw Adressen verknüft werden.\
Zur Verwendung von Aktivitäten ist eine PRO-Lizenz für Monkey Office notwendig.\
Ohne PRO-Lizenz lassen sich Aktivitäten nicht mehr weiterverarbeiten!
:::

[]{#aktivitaet_Datenstrukturen .anchor}

### Datenstrukturen von Aktivitaet

[]{#Parameter_AktivitaetArt .anchor}

::: jsonproto
[AktivitaetArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"AktivitaetArt\"]{.jsonkey tag="AktivitaetArt"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                           |   Aufzählung, Integer                 1=[Telefon]{tag="Telefon"}\         |
|                                                                           |                                       2=[Besuch]{tag="Besuch"}\           |
|                                                                           |                                       3=[Email]{tag="Email"}\             |
|                                                                           |                                       4=[Brief]{tag="Brief"}\             |
|                                                                           |                                       5=[Sonstiges]{tag="Sonstiges"}\     |
|                                                                           |                                       6=[Notiz]{tag="Notiz"}              |
|                                                                           |                                                                           |
|                                                                           |   ----------------------------------- ----------------------------------- |
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_AktivitaetListItem .anchor}

::: jsonproto
[AktivitaetListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                |
|                                                                                                                                  |
|   ----------------------------------------------------------------- ------------------------------------------------------------ |
|     [\"Aktivitaet_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string, readonly                                             |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                       |
|     [\"AdressMatchCode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string, readonly                                             |
|     [\"Betreff\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                       |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                date (yyyy-mm-dd)                                            |
|     [\"AktivitaetArt\"]{.jsonkey}: [ \... ]{.jsonvalue}             [AktivitaetArt](#Parameter_AktivitaetArt){.navlinkcomment}   |
|   ----------------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                                  |
| }                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AktivitaetItem .anchor}

::: jsonproto
[AktivitaetItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                |
|                                                                                                                                  |
|   ----------------------------------------------------------------- ------------------------------------------------------------ |
|     [\"Aktivitaet_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string, readonly                                             |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                       |
|     [\"AdressMatchCode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string, readonly                                             |
|     [\"Betreff\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                       |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                date (yyyy-mm-dd)                                            |
|     [\"AktivitaetArt\"]{.jsonkey}: [ \... ]{.jsonvalue},            [AktivitaetArt](#Parameter_AktivitaetArt){.navlinkcomment}   |
|     [\"VersionKey\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string, readonly                                             |
|     [\"ProjektName\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string, readonly                                             |
|     [\"Artbezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string, readonly                                             |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                       |
|     [\"Bearbeiter\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}            string                                                       |
|   ----------------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                                  |
| }                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AktivitaetFilter .anchor}

::: jsonproto
[AktivitaetFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------+
| {                                                                                        |
|                                                                                          |
|   -------------------------------------------------------------- ----------------------- |
|     [\"Suchtext\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                  |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                  |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          date (yyyy-mm-dd)       |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          date (yyyy-mm-dd)       |
|     [\"AdressMatchCode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                  |
|     [\"ProjektName\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                  |
|     [\"Telefonat\"]{.jsonkey}: [ \... ]{.jsonvalue},             boolean (true\|false)   |
|     [\"Besuch\"]{.jsonkey}: [ \... ]{.jsonvalue},                boolean (true\|false)   |
|     [\"E-Mail\"]{.jsonkey}: [ \... ]{.jsonvalue},                boolean (true\|false)   |
|     [\"Brief\"]{.jsonkey}: [ \... ]{.jsonvalue},                 boolean (true\|false)   |
|     [\"Notiz\"]{.jsonkey}: [ \... ]{.jsonvalue},                 boolean (true\|false)   |
|     [\"Sonstiges\"]{.jsonkey}: [ \... ]{.jsonvalue},             boolean (true\|false)   |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                  |
|     [\"Bearbeiter\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}         string                  |
|   -------------------------------------------------------------- ----------------------- |
|                                                                                          |
| }                                                                                        |
+------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AktivitaetAddItem .anchor}

::: jsonproto
[AktivitaetAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                |
|                                                                                                                                  |
|   ----------------------------------------------------------------- ------------------------------------------------------------ |
|     [\"AktivitaetArt\"]{.jsonkey}: [ \... ]{.jsonvalue},            [AktivitaetArt](#Parameter_AktivitaetArt){.navlinkcomment}   |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                       |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                date (yyyy-mm-dd)                                            |
|     [\"Betreff\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                       |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                       |
|     [\"Bearbeiter\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}            string                                                       |
|   ----------------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                                  |
| }                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#aktivitaet .anchor}\

### Funktionsliste von Aktivitaet

[]{#aktivitaet_aktivitaetFilterTemplate .anchor}

::::: memitem
::: memproto
[aktivitaetFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Aktivität-Filter

**Aufruf:**
:   { \"aktivitaetFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"aktivitaetFilterTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                     |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AktivitaetFilter\": {\...} } ]{.jsonvalue}   [AktivitaetFilter](#Parameter_AktivitaetFilter){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                                       |
    | }                                                                                                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#aktivitaet_aktivitaetList .anchor}

::::: memitem
::: memproto
[aktivitaetList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Listet vorhandene Aktivitäten

**Aufruf:**
:   { \"aktivitaetList\":
    +--------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                          |
    |   ---------------------------------------------------------- ----------------------------------------------------------------------------- |
    |     [\"AktivitaetFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AktivitaetFilter](#Parameter_AktivitaetFilter){.navlinkcomment} (optional)   |
    |   ---------------------------------------------------------- ----------------------------------------------------------------------------- |
    |                                                                                                                                            |
    | }                                                                                                                                          |
    +--------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"aktivitaetListResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AktivitaetListItem\": {\...} } ]{.jsonvalue}   [AktivitaetListItem](#Parameter_AktivitaetListItem){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#aktivitaet_aktivitaetGet .anchor}

::::: memitem
::: memproto
[aktivitaetGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert ein Aktivität für die ID

**Aufruf:**
:   { \"aktivitaetGet\":
    +------------------------------------------------------------------------+
    | {                                                                      |
    |   ----------------------------------------------------------- -------- |
    |     [\"Aktivitaet_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ----------------------------------------------------------- -------- |
    |                                                                        |
    | }                                                                      |
    +------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"aktivitaetGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                               |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AktivitaetItem\": {\...} } ]{.jsonvalue}   [AktivitaetItem](#Parameter_AktivitaetItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |                                                                                                                                                 |
    | }                                                                                                                                               |
    +-------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#aktivitaet_aktivitaetModify .anchor}

::::: memitem
::: memproto
[aktivitaetModify]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
modifiziert vorhandene Aktivität, der Ablauf erfolgt ähnlich dem von Verkaufsbelegen

**Aufruf:**
:   { \"aktivitaetModify\":
    +---------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                         |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |     [\"AktivitaetItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AktivitaetItem](#Parameter_AktivitaetItem){.navlinkcomment}   |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |                                                                                                                           |
    | }                                                                                                                         |
    +---------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"aktivitaetModifyResponse\":
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

[]{#aktivitaet_aktivitaetTemplate .anchor}

::::: memitem
::: memproto
[aktivitaetTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert AktivitaetAddItem als Vorlage

**Aufruf:**
:   { \"aktivitaetTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"aktivitaetTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                        |
    |   --------------------------------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AktivitaetAddItem\": {\...} } ]{.jsonvalue}   [AktivitaetAddItem](#Parameter_AktivitaetAddItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                                          |
    | }                                                                                                                                                        |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#aktivitaet_aktivitaetAdd .anchor}

::::: memitem
::: memproto
[aktivitaetAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt ein neues Aktivität hinzu

**Aufruf:**
:   { \"aktivitaetAdd\":
    +------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                  |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"AktivitaetAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AktivitaetAddItem](#Parameter_AktivitaetAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                    |
    | }                                                                                                                                  |
    +------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"aktivitaetAddResponse\":
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

[]{#aktivitaet_aktivitaetDelete .anchor}

::::: memitem
::: memproto
[aktivitaetDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht ein vorhandenes Aktivität

**Aufruf:**
:   { \"aktivitaetDelete\":
    +------------------------------------------------------------------------+
    | {                                                                      |
    |   ----------------------------------------------------------- -------- |
    |     [\"Aktivitaet_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ----------------------------------------------------------- -------- |
    |                                                                        |
    | }                                                                      |
    +------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"aktivitaetDeleteResponse\":
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

[]{#Content_attachment .anchor}  \

