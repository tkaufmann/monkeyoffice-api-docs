## Attachment-Verwaltung

::: mohelpinfo
\
Die Zuweisung von Attachments zu Datenobjekten erfolgt in dem jeweilen Modul,z.B über die Funktion verkaufbelegAddAttachment im Modul Verkaufsbelege (siehe dortige Beschreibung). Attachment-Daten werden als Base64-Daten übertragen.\
Ab Version 17.0 werden alternativ Links unterstützt. Links verweisen auf Daten, welche durch externe System verwaltet werden.\
Über die Attachment-Verwaltung können existierende Attachments aufgelistet und abgerufen werden.\
Die SourceID wird je nach Parent-Objekt (AttachmentGruppe) interpretiert (Verkaufsbelege=Verkaufbeleg_ID).
:::

[]{#attachment_Datenstrukturen .anchor}

### Datenstrukturen von Attachment-Verwaltung

[]{#Parameter_AttachmentGruppe .anchor}

::: jsonproto
[AttachmentGruppe]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| { [\"AttachmentGruppe\"]{.jsonkey tag="AttachmentGruppe"}: [\...]{.jsonvalue} } |   ----------------------------------- ------------------------------------------------------------ |
|                                                                                 |   Aufzählung, Integer                 1=[Buchungen]{tag="Buchungen"}\                              |
|                                                                                 |                                       2=[Verkaufsbelege]{tag="Verkaufsbelege"}\                    |
|                                                                                 |                                       3=[Einkaufsbelege]{tag="Einkaufsbelege"}\                    |
|                                                                                 |                                       4=[Offene Posten]{tag="Offene Posten"}\                      |
|                                                                                 |                                       5=[Adressen]{tag="Adressen"}\                                |
|                                                                                 |                                       10=[Artikel und Leistungen]{tag="Artikel und Leistungen"}\   |
|                                                                                 |                                       15=[Verkaufsposition]{tag="Verkaufsposition"}\               |
|                                                                                 |                                       16=[Einkaufsposition]{tag="Einkaufsposition"}\               |
|                                                                                 |                                       21=[Projekte]{tag="Projekte"}                                |
|                                                                                 |                                                                                                    |
|                                                                                 |   ----------------------------------- ------------------------------------------------------------ |
+---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AttachmentFilter .anchor}

::: jsonproto
[AttachmentFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                              |
|                                                                                                                                |
|   ------------------------------------------------------------- -------------------------------------------------------------- |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         date (yyyy-mm-dd), Attachment hinzugefuegt                     |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         date (yyyy-mm-dd), Attachment hinzugefuegt                     |
|     [\"DatumVonParent\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   date (yyyy-mm-dd), Neu ab 20.1.0, bezogen auf ElternDokument   |
|     [\"DatumBisParent\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   date (yyyy-mm-dd), Neu ab 20.1.0, bezogen auf ElternDokument   |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                         |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                         |
|     [\"Dateityp\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                         |
|     [\"AttachmentGruppe\"]{.jsonkey}: [ \... ]{.jsonvalue},     integer                                                        |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                         |
|     [\"Link\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}              string                                                         |
|   ------------------------------------------------------------- -------------------------------------------------------------- |
|                                                                                                                                |
| }                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AttachmentListItem .anchor}

::: jsonproto
[AttachmentListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                 |
|                                                                                                                                                   |
|   ------------------------------------------------------------ ---------------------------------------------------------------------------------- |
|     [\"Attachment_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                             |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                                             |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string, Dateiname der Raw-Daten, wird bei Links nicht benutzt                      |
|     [\"AttachmentGruppe\"]{.jsonkey}: [ \... ]{.jsonvalue},    [AttachmentGruppe](#Parameter_AttachmentGruppe){.navlinkcomment}                   |
|     [\"SourceID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string, wird entsprechend der Gruppe interpretiert,z.B Verkauf = Verkaufbeleg_ID   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           date (yyyy-mm-dd)                                                                  |
|     [\"Dateityp\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                             |
|     [\"Dateigroesse\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                                            |
|     [\"Link\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}             string                                                                             |
|   ------------------------------------------------------------ ---------------------------------------------------------------------------------- |
|                                                                                                                                                   |
| }                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AttachmentItem .anchor}

::: jsonproto
[AttachmentItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                 |
|                                                                                                                                                   |
|   ------------------------------------------------------------ ---------------------------------------------------------------------------------- |
|     [\"Attachment_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                             |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                                             |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string, Dateiname der Raw-Daten, wird bei Links nicht benutzt                      |
|     [\"AttachmentGruppe\"]{.jsonkey}: [ \... ]{.jsonvalue},    [AttachmentGruppe](#Parameter_AttachmentGruppe){.navlinkcomment}                   |
|     [\"SourceID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string, wird entsprechend der Gruppe interpretiert,z.B Verkauf = Verkaufbeleg_ID   |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           date (yyyy-mm-dd)                                                                  |
|     [\"Dateityp\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                                             |
|     [\"Dateigroesse\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                                            |
|     [\"Link\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                                             |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}          string                                                                             |
|   ------------------------------------------------------------ ---------------------------------------------------------------------------------- |
|                                                                                                                                                   |
| }                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AttachmentItemData .anchor}

::: jsonproto
[AttachmentItemData]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                |
|                                                                                                                                  |
|   ----------------------------------------------------------- ------------------------------------------------------------------ |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                             |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string, Dateiname der Raw-Daten, wird bei Links nicht benutzt      |
|     [\"AttachmentGruppe\"]{.jsonkey}: [ \... ]{.jsonvalue},   [AttachmentGruppe](#Parameter_AttachmentGruppe){.navlinkcomment}   |
|     [\"Dateigroesse\"]{.jsonkey}: [ \... ]{.jsonvalue},       integer                                                            |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          date (yyyy-mm-dd)                                                  |
|     [\"Dateityp\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                             |
|     [\"DatenBASE64\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string, Raw-Daten in BASE64-Kodierung                              |
|     [\"Link\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                             |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}         string                                                             |
|   ----------------------------------------------------------- ------------------------------------------------------------------ |
|                                                                                                                                  |
| }                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_AttachmentAddItem .anchor}

::: jsonproto
[AttachmentAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                            |
|                                                                                                                              |
|   ---------------------------------------------------------- --------------------------------------------------------------- |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                          |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string, Dateiname der Raw-Daten, wird bei Links nicht benutzt   |
|     [\"DatenBASE64\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string, Raw-Daten in BASE64-Kodierung                           |
|     [\"Link\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                          |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}        string                                                          |
|   ---------------------------------------------------------- --------------------------------------------------------------- |
|                                                                                                                              |
| }                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#attachment .anchor}\

### Funktionsliste von Attachment-Verwaltung

[]{#attachment_attachmentFilterTemplate .anchor}

::::: memitem
::: memproto
[attachmentFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Attachment-Filter

**Aufruf:**
:   { \"attachmentFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"attachmentFilterTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                     |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AttachmentFilter\": {\...} } ]{.jsonvalue}   [AttachmentFilter](#Parameter_AttachmentFilter){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                                       |
    | }                                                                                                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#attachment_attachmentList .anchor}

::::: memitem
::: memproto
[attachmentList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
listet vorhandenen Attachments

**Aufruf:**
:   { \"attachmentList\":
    +--------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                          |
    |   ---------------------------------------------------------- ----------------------------------------------------------------------------- |
    |     [\"AttachmentFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AttachmentFilter](#Parameter_AttachmentFilter){.navlinkcomment} (optional)   |
    |   ---------------------------------------------------------- ----------------------------------------------------------------------------- |
    |                                                                                                                                            |
    | }                                                                                                                                          |
    +--------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"attachmentListResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AttachmentListItem\": {\...} } ]{.jsonvalue}   [AttachmentListItem](#Parameter_AttachmentListItem){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#attachment_attachmentGet .anchor}

::::: memitem
::: memproto
[attachmentGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details eines Attachments

**Aufruf:**
:   { \"attachmentGet\":
    +------------------------------------------------------------------------+
    | {                                                                      |
    |   ----------------------------------------------------------- -------- |
    |     [\"Attachment_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ----------------------------------------------------------- -------- |
    |                                                                        |
    | }                                                                      |
    +------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"attachmentGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                               |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AttachmentItem\": {\...} } ]{.jsonvalue}   [AttachmentItem](#Parameter_AttachmentItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |                                                                                                                                                 |
    | }                                                                                                                                               |
    +-------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#attachment_attachmentLoad .anchor}

::::: memitem
::: memproto
[attachmentLoad]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Download Attachment-File. Die Daten des Dokuments sind als Base64 codiert

**Aufruf:**
:   { \"attachmentLoad\":
    +------------------------------------------------------------------------+
    | {                                                                      |
    |   ----------------------------------------------------------- -------- |
    |     [\"Attachment_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ----------------------------------------------------------- -------- |
    |                                                                        |
    | }                                                                      |
    +------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"attachmentLoadResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"AttachmentItemData\": {\...} } ]{.jsonvalue}   [AttachmentItemData](#Parameter_AttachmentItemData){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#attachment_attachmentDelete .anchor}

::::: memitem
::: memproto
[attachmentDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht ein Attachment

**Aufruf:**
:   { \"attachmentDelete\":
    +------------------------------------------------------------------------+
    | {                                                                      |
    |   ----------------------------------------------------------- -------- |
    |     [\"Attachment_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ----------------------------------------------------------- -------- |
    |                                                                        |
    | }                                                                      |
    +------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"attachmentDeleteResponse\":
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

[]{#Content_apiinfo .anchor}  \

