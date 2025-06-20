## Projekte

::: mohelpinfo
\
Diese Modul erlaubt das Auflisten und Abrufen (vorhandener) Projekt. Über Projekte können z.B. Belege für Einkauf/Verkauf organisiert werden.\
Zur Verwendung von Projekten ist eine PRO-Lizenz für Monkey Office notwendig.\
Ohne PRO-Lizenz lassen sich Datensätze, welche Projekten zugeordnet sind, nicht mehr weiterverarbeiten!
:::

[]{#projekte_Datenstrukturen .anchor}

### Datenstrukturen von Projekte

[]{#Parameter_ProjektStatus .anchor}

::: jsonproto
[ProjektStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| { [\"ProjektStatus\"]{.jsonkey tag="ProjektStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- ---------------------------------------- |
|                                                                           |   Aufzählung, Integer                 0=[]{tag=""}\                            |
|                                                                           |                                       1=[Akquise]{tag="Akquise"}\              |
|                                                                           |                                       2=[Beauftragt]{tag="Beauftragt"}\        |
|                                                                           |                                       3=[Vorbereitung]{tag="Vorbereitung"}\    |
|                                                                           |                                       4=[In Arbeit]{tag="In Arbeit"}\          |
|                                                                           |                                       5=[Abrechnen]{tag="Abrechnen"}\          |
|                                                                           |                                       6=[Abgeschlossen]{tag="Abgeschlossen"}   |
|                                                                           |                                                                                |
|                                                                           |   ----------------------------------- ---------------------------------------- |
+---------------------------------------------------------------------------+--------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ProjektListItem .anchor}

::: jsonproto
[ProjektListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                         |
|                                                                                                                           |
|   ---------------------------------------------------------- ------------------------------------------------------------ |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                       |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                       |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                       |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      date (yyyy-mm-dd)                                            |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      date (yyyy-mm-dd)                                            |
|     [\"ProjektStatus\"]{.jsonkey}: [ \... ]{.jsonvalue}      [ProjektStatus](#Parameter_ProjektStatus){.navlinkcomment}   |
|   ---------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                           |
| }                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ProjektItem .anchor}

::: jsonproto
[ProjektItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                             |
|                                                                                                                               |
|   -------------------------------------------------------------- ------------------------------------------------------------ |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                       |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                       |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                       |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          date (yyyy-mm-dd)                                            |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          date (yyyy-mm-dd)                                            |
|     [\"ProjektStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},         [ProjektStatus](#Parameter_ProjektStatus){.navlinkcomment}   |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                       |
|     [\"Bearbeiter\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                       |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"EtikettTag\"]{.jsonkey}: [\...]{.jsonvalue},              [EtikettTags](#Parameter_EtikettTags){.navlinkcomment}       |
|     [\"AttachmentIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue}   Array vom Typ string, readonly                               |
|   -------------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                               |
| }                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ProjektFilter .anchor}

::: jsonproto
[ProjektFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------+
| {                                                                                     |
|                                                                                       |
|   ----------------------------------------------------------- ----------------------- |
|     [\"Suchtext\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                  |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       date (yyyy-mm-dd)       |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       date (yyyy-mm-dd)       |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                  |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                  |
|     [\"KeinStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)   |
|     [\"Akquise\"]{.jsonkey}: [ \... ]{.jsonvalue},            boolean (true\|false)   |
|     [\"Beauftragt\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)   |
|     [\"Vorbereitung\"]{.jsonkey}: [ \... ]{.jsonvalue},       boolean (true\|false)   |
|     [\"InArbeit\"]{.jsonkey}: [ \... ]{.jsonvalue},           boolean (true\|false)   |
|     [\"Abrechnen\"]{.jsonkey}: [ \... ]{.jsonvalue},          boolean (true\|false)   |
|     [\"Abgeschlossen\"]{.jsonkey}: [ \... ]{.jsonvalue},      boolean (true\|false)   |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                  |
|     [\"Bearbeiter\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                  |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                  |
|     [\"EtikettTag_Ohne\"]{.jsonkey}: [ \... ]{.jsonvalue},    boolean (true\|false)   |
|     [\"EtikettTag_1\"]{.jsonkey}: [ \... ]{.jsonvalue},       boolean (true\|false)   |
|     [\"EtikettTag_2\"]{.jsonkey}: [ \... ]{.jsonvalue},       boolean (true\|false)   |
|     [\"EtikettTag_3\"]{.jsonkey}: [ \... ]{.jsonvalue},       boolean (true\|false)   |
|     [\"EtikettTag_4\"]{.jsonkey}: [ \... ]{.jsonvalue},       boolean (true\|false)   |
|     [\"EtikettTag_5\"]{.jsonkey}: [ \... ]{.jsonvalue},       boolean (true\|false)   |
|     [\"EtikettTag_6\"]{.jsonkey}: [ \... ]{.jsonvalue},       boolean (true\|false)   |
|     [\"EtikettTag_7\"]{.jsonkey}: [ \... ]{.jsonvalue}        boolean (true\|false)   |
|   ----------------------------------------------------------- ----------------------- |
|                                                                                       |
| }                                                                                     |
+---------------------------------------------------------------------------------------+
:::

\
[]{#projekte .anchor}\

### Funktionsliste von Projekte

[]{#projekte_projektFilterTemplate .anchor}

::::: memitem
::: memproto
[projektFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Projekt-Filter

**Aufruf:**
:   { \"projektFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"projektFilterTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                            |
    |   ----------------------------------------------------------------------------- ------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ProjektFilter\": {\...} } ]{.jsonvalue}   [ProjektFilter](#Parameter_ProjektFilter){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------- ------------------------------------------------------------ |
    |                                                                                                                                              |
    | }                                                                                                                                            |
    +----------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#projekte_projektList .anchor}

::::: memitem
::: memproto
[projektList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Listet vorhandene Projekte

**Aufruf:**
:   { \"projektList\":
    +-----------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                 |
    |   ------------------------------------------------------- ----------------------------------------------------------------------- |
    |     [\"ProjektFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [ProjektFilter](#Parameter_ProjektFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------- ----------------------------------------------------------------------- |
    |                                                                                                                                   |
    | }                                                                                                                                 |
    +-----------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"projektListResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                  |
    |   ------------------------------------------------------------------------------- ---------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ProjektListItem\": {\...} } ]{.jsonvalue}   [ProjektListItem](#Parameter_ProjektListItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------- ---------------------------------------------------------------- |
    |                                                                                                                                                    |
    | }                                                                                                                                                  |
    +----------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#projekte_projektGet .anchor}

::::: memitem
::: memproto
[projektGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert ein Projekt für die ID

**Aufruf:**
:   { \"projektGet\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"projektGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                      |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ProjektItem\": {\...} } ]{.jsonvalue}   [ProjektItem](#Parameter_ProjektItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |                                                                                                                                        |
    | }                                                                                                                                      |
    +----------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#projekte_projektAddAttachment .anchor}

::::: memitem
::: memproto
[projektAddAttachment]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt ein Attachment einem Projekt hinzu

**Aufruf:**
:   { \"projektAddAttachment\":
    +------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                  |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                               |
    |     [\"AttachmentAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AttachmentAddItem](#Parameter_AttachmentAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                    |
    | }                                                                                                                                  |
    +------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"projektAddAttachmentResponse\":
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

[]{#Content_aktivitaet .anchor}  \

