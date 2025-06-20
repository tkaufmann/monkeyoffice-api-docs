## Verkaufsbelege

[]{#verkauf_Datenstrukturen .anchor}

### Datenstrukturen von Verkaufsbelege

[]{#Parameter_VerkaufbelegArt .anchor}

::: jsonproto
[VerkaufbelegArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: jsondoc
::: mohelpinfo
Neu ab 21.2.0, Belegart Kostenvoranschlag
:::

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| { [\"VerkaufbelegArt\"]{.jsonkey tag="VerkaufbelegArt"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------------------- |
|                                                                               |   Aufzählung, Integer                 1=[Angebot]{tag="Angebot"}\                         |
|                                                                               |                                       2=[Auftragbestätigung]{tag="Auftragbestätigung"}\   |
|                                                                               |                                       3=[Lieferschein]{tag="Lieferschein"}\               |
|                                                                               |                                       4=[Rechnung]{tag="Rechnung"}\                       |
|                                                                               |                                       5=[Abschlagsrechnung]{tag="Abschlagsrechnung"}\     |
|                                                                               |                                       6=[Korrekturrechnung]{tag="Korrekturrechnung"}\     |
|                                                                               |                                       7=[Proforma-Rechnung]{tag="Proforma-Rechnung"}\     |
|                                                                               |                                       8=[Storno]{tag="Storno"}\                           |
|                                                                               |                                       9=[Kostenvoranschlag]{tag="Kostenvoranschlag"}      |
|                                                                               |                                                                                           |
|                                                                               |   ----------------------------------- --------------------------------------------------- |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
::::

\
[]{#Parameter_VerkaufbelegStatus .anchor}

::: jsonproto
[VerkaufbelegStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| { [\"VerkaufbelegStatus\"]{.jsonkey tag="VerkaufbelegStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------------------- |
|                                                                                     |   Aufzählung, Integer                 1=[Alle]{tag="Alle"}\                                    |
|                                                                                     |                                       2=[Nur Dokumente]{tag="Nur Dokumente"}\                  |
|                                                                                     |                                       3=[Nur Entwürfe/Vorlagen]{tag="Nur Entwürfe/Vorlagen"}   |
|                                                                                     |                                                                                                |
|                                                                                     |   ----------------------------------- -------------------------------------------------------- |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufbelegDruckstatus .anchor}

::: jsonproto
[VerkaufbelegDruckstatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| { [\"VerkaufbelegDruckstatus\"]{.jsonkey tag="VerkaufbelegDruckstatus"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------------- |
|                                                                                               |   Aufzählung, Integer                 0=[Alle]{tag="Alle"}\                         |
|                                                                                               |                                       1=[nur ungedruckte]{tag="nur ungedruckte"}\   |
|                                                                                               |                                       2=[nur gedruckte]{tag="nur gedruckte"}        |
|                                                                                               |                                                                                     |
|                                                                                               |   ----------------------------------- --------------------------------------------- |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufBelegKalkbasis .anchor}

::: jsonproto
[VerkaufBelegKalkbasis]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"VerkaufBelegKalkbasis\"]{.jsonkey tag="VerkaufBelegKalkbasis"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                           |   Aufzählung, Integer                 0=[Netto]{tag="Netto"}\             |
|                                                                                           |                                       1=[Brutto]{tag="Brutto"}            |
|                                                                                           |                                                                           |
|                                                                                           |   ----------------------------------- ----------------------------------- |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufbelegPositionArt .anchor}

::: jsonproto
[VerkaufbelegPositionArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| { [\"VerkaufbelegPositionArt\"]{.jsonkey tag="VerkaufbelegPositionArt"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------------------------------------------- |
|                                                                                               |   Aufzählung, Integer                 1=[Stammartikel]{tag="Stammartikel"}\                                       |
|                                                                                               |                                       7=[Alternativer Stammartikel]{tag="Alternativer Stammartikel"}\             |
|                                                                                               |                                       2=[Manueller Artikel]{tag="Manueller Artikel"}\                             |
|                                                                                               |                                       8=[Alternativer manueller Artikel]{tag="Alternativer manueller Artikel"}\   |
|                                                                                               |                                       3=[Textposition]{tag="Textposition"}\                                       |
|                                                                                               |                                       4=[Zwischensumme]{tag="Zwischensumme"}\                                     |
|                                                                                               |                                       5=[Seitenumbruch]{tag="Seitenumbruch"}\                                     |
|                                                                                               |                                       6=[Kommentar]{tag="Kommentar"}                                              |
|                                                                                               |                                                                                                                   |
|                                                                                               |   ----------------------------------- --------------------------------------------------------------------------- |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufVorbelegStatus .anchor}

::: jsonproto
[VerkaufVorbelegStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: jsondoc
::: mohelpinfo
Neu ab 18.3.0
:::

+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| { [\"VerkaufVorbelegStatus\"]{.jsonkey tag="VerkaufVorbelegStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- ---------------------------------------------------- |
|                                                                                           |   Aufzählung, Integer                 0=[Alle Belege]{tag="Alle Belege"}\                  |
|                                                                                           |                                       1=[hat Vorbelege]{tag="hat Vorbelege"}\              |
|                                                                                           |                                       2=[hat keine Vorbelege]{tag="hat keine Vorbelege"}   |
|                                                                                           |                                                                                            |
|                                                                                           |   ----------------------------------- ---------------------------------------------------- |
+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
::::

\
[]{#Parameter_VerkaufFolgebelegStatus .anchor}

::: jsonproto
[VerkaufFolgebelegStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: jsondoc
::: mohelpinfo
Neu ab 18.3.0
:::

+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| { [\"VerkaufFolgebelegStatus\"]{.jsonkey tag="VerkaufFolgebelegStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------------------- |
|                                                                                               |   Aufzählung, Integer                 0=[Alle Belege]{tag="Alle Belege"}\                      |
|                                                                                               |                                       1=[hat Folgebelege]{tag="hat Folgebelege"}\              |
|                                                                                               |                                       2=[hat keine Folgebelege]{tag="hat keine Folgebelege"}   |
|                                                                                               |                                                                                                |
|                                                                                               |   ----------------------------------- -------------------------------------------------------- |
+-----------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
::::

\
[]{#Parameter_VerkaufbelegFilter .anchor}

::: jsonproto
[VerkaufbelegFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                 |
|                                                                                                                                                                                   |
|   ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------ |
|     [\"Suchtext\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                                                       |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                                                                       |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              date (yyyy-mm-dd)                                                                                            |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              date (yyyy-mm-dd)                                                                                            |
|     [\"Kostenvoranschlag\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false), Neu ab 21.2.0                                                                         |
|     [\"Angebot\"]{.jsonkey}: [ \... ]{.jsonvalue},                   boolean (true\|false)                                                                                        |
|     [\"AuftragsBestaetigung\"]{.jsonkey}: [ \... ]{.jsonvalue},      boolean (true\|false)                                                                                        |
|     [\"Lieferschein\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"ProformaRechnung\"]{.jsonkey}: [ \... ]{.jsonvalue},          boolean (true\|false)                                                                                        |
|     [\"Rechnung\"]{.jsonkey}: [ \... ]{.jsonvalue},                  boolean (true\|false)                                                                                        |
|     [\"AbschlagsRechnung\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)                                                                                        |
|     [\"KorrekturRechnung\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)                                                                                        |
|     [\"Storno\"]{.jsonkey}: [ \... ]{.jsonvalue},                    boolean (true\|false)                                                                                        |
|     [\"Schlussrechnung\"]{.jsonkey}: [ \... ]{.jsonvalue},           boolean (true\|false), Neu ab 21.0                                                                           |
|     [\"VerkaufbelegStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},        [VerkaufbelegStatus](#Parameter_VerkaufbelegStatus){.navlinkcomment}                                         |
|     [\"VerkaufbelegDruckstatus\"]{.jsonkey}: [ \... ]{.jsonvalue},   [VerkaufbelegDruckstatus](#Parameter_VerkaufbelegDruckstatus){.navlinkcomment}                               |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},         [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}                                           |
|     [\"AuftragsNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                                                                       |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string, Neu ab 16.0.1,ersetzt BestellNr                                                                      |
|     [\"Betreff\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},               string                                                                                                       |
|     [\"Anschrift\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                                                       |
|     [\"KopfText\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                                                       |
|     [\"FussText\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                                                       |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                                                       |
|     [\"Bearbeiter\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                                                                       |
|     [\"Notiz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                 string                                                                                                       |
|     [\"EtikettTag_Ohne\"]{.jsonkey}: [ \... ]{.jsonvalue},           boolean (true\|false)                                                                                        |
|     [\"EtikettTag_1\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"EtikettTag_2\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"EtikettTag_3\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"EtikettTag_4\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"EtikettTag_5\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"EtikettTag_6\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"EtikettTag_7\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"MitVorbelege\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false), wird ab 18.3 nicht mehr ausgewertet und entfällt ab 19.0, VorbelegStatus benutzen     |
|     [\"MitFolgebelege\"]{.jsonkey}: [ \... ]{.jsonvalue},            boolean (true\|false), wird ab 18.3 nicht mehr ausgewertet und entfällt ab 19.0, FolgebelegStatus benutzen   |
|     [\"Zahlungstatus\"]{.jsonkey}: [ \... ]{.jsonvalue},             [Zahlungstatus](#Parameter_Zahlungstatus){.navlinkcomment}                                                   |
|     [\"Versandnummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string, Neu ab 17.1                                                                                          |
|     [\"VorbelegStatus\"]{.jsonkey}: [\...]{.jsonvalue},              [VerkaufVorbelegStatus](#Parameter_VerkaufVorbelegStatus){.navlinkcomment}, Neu ab 18.3                      |
|     [\"FolgebelegStatus\"]{.jsonkey}: [\...]{.jsonvalue}             [VerkaufFolgebelegStatus](#Parameter_VerkaufFolgebelegStatus){.navlinkcomment}, Neu ab 18.3                  |
|   ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                                                   |
| }                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufbelegListitem .anchor}

::: jsonproto
[VerkaufbelegListitem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                 |
|                                                                                                                                   |
|   -------------------------------------------------------------- ---------------------------------------------------------------- |
|     [\"Verkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                           |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                           |
|     [\"AuftragNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                           |
|     [\"VerkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue},       [VerkaufbelegArt](#Parameter_VerkaufbelegArt){.navlinkcomment}   |
|     [\"Kunde\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                           |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             date (yyyy-mm-dd)                                                |
|     [\"Lieferdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       date (yyyy-mm-dd)                                                |
|     [\"GesamtNettoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                           |
|     [\"GesamtBruttoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                           |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                           |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}          string                                                           |
|   -------------------------------------------------------------- ---------------------------------------------------------------- |
|                                                                                                                                   |
| }                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufbelegItem .anchor}

::: jsonproto
[VerkaufbelegItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                 |
|   ------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------- |
|     [\"Verkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string, readonly                                                                                           |
|     [\"VersionKey\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string, readonly                                                                                           |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string, readonly                                                                                           |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                    string                                                                                                     |
|     [\"AuftragNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, readonly                                                                                           |
|     [\"VerkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                           [VerkaufbelegArt](#Parameter_VerkaufbelegArt){.navlinkcomment}, readonly                                   |
|     [\"Kunde\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string, readonly                                                                                           |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 date (yyyy-mm-dd), readonly                                                                                |
|     [\"Lieferdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           date (yyyy-mm-dd), readonly                                                                                |
|     [\"GesamtNettoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                         string, readonly                                                                                           |
|     [\"GesamtBruttoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string, readonly                                                                                           |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, readonly                                                                                           |
|     [\"Entwurf\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                   boolean (true\|false), readonly                                                                            |
|     [\"EtikettTag\"]{.jsonkey}: [\...]{.jsonvalue},                                                                  [EtikettTags](#Parameter_EtikettTags){.navlinkcomment}                                                     |
|     [\"Zahlungstatus\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                             [Zahlungstatus](#Parameter_Zahlungstatus){.navlinkcomment}, readonly                                       |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                         [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}, readonly                               |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string, readonly                                                                                           |
|     [\"RechnAnschrift\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string                                                                                                     |
|     [\"LieferAnschrift\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string                                                                                                     |
|     [\"LaVerwenden\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                               boolean (true\|false)                                                                                      |
|     [\"Betreff\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                                     |
|     [\"Anrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                string                                                                                                     |
|     [\"KopfText\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string                                                                                                     |
|     [\"FussText\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string                                                                                                     |
|     [\"Grussformel\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           string                                                                                                     |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                                     |
|     [\"Bearbeiter\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string                                                                                                     |
|     [\"BearbeiterAngeben\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                         boolean (true\|false)                                                                                      |
|     [\"Steuergebiet\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                              [Steuergebiet](#Parameter_Steuergebiet){.navlinkcomment}, readonly                                         |
|     [\"VKPreisliste_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string, readonly, überschreibt Preisliste der Adresse                                                      |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string, readonly                                                                                           |
|     [\"GesamtNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                         string, readonly                                                                                           |
|     [\"GesamtBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"GesamtRabattFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"GesamtSteuerFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"GesamtRabattSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"GesamtSteuerSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"Zahlungsbedingungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                   string, readonly                                                                                           |
|     [\"SepaMandatReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                    string, readonly                                                                                           |
|     [\"SepaBankeinzug\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        date (yyyy-mm-dd), readonly                                                                                |
|     [\"Lieferart\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string                                                                                                     |
|     [\"Versandnummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                         string                                                                                                     |
|     [\"VersandURL\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string                                                                                                     |
|     [\"Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                string, readonly                                                                                           |
|     [\"VorbelegIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},                                                        Array vom Typ string, readonly                                                                             |
|     [\"AttachmentIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},                                                      Array vom Typ string, readonly                                                                             |
|     [\"Posten_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, readonly                                                                                           |
|     [\"Belegausgabe\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                              [BelegAusgabe](#Parameter_BelegAusgabe){.navlinkcomment}, readonly, neu ab Version 22.0                    |
|     [\"AbrZeitraumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        date (yyyy-mm-dd), readonly, neu ab Version 22.1                                                           |
|     [\"AbrZeitraumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        date (yyyy-mm-dd), readonly, neu ab Version 22.1                                                           |
|     [\"ER_DatumFaellig\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       date (yyyy-mm-dd), readonly, neu ab Version 22.1                                                           |
|     [\"ER_ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                          string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_VertragNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                          string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_AuftragNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                          string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_VergabeNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                          string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_Objektkennung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                      string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_Bemerkungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_LeitwegID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                          string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_GrundZuAbschlag\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                    string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_VorgaengerRechnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                 string, readonly, neu ab Version 22.1                                                                      |
|     [\"ER_Verwendungszweck\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                   string, readonly, neu ab Version 22.1                                                                      |
|     [\"VerkaufbelegPositionItemList\"]{.jsonkey}: [ { \"VerkaufbelegPositionItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [VerkaufbelegPositionItem](#Parameter_VerkaufbelegPositionItem){.navlinkcomment}, readonly   |
|   ------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                 |
| }                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufbelegPositionItem .anchor}

::: jsonproto
[VerkaufbelegPositionItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                               |
|                                                                                                                                                                 |
|   ---------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|     [\"Nummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                           |
|     [\"PosNrManuell\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                    string                                                                           |
|     [\"VerkaufbelegPositionArt\"]{.jsonkey}: [ \... ]{.jsonvalue},             [VerkaufbelegPositionArt](#Parameter_VerkaufbelegPositionArt){.navlinkcomment}   |
|     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                           |
|     [\"ArtikelArt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                           |
|     [\"ArtikelNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                       string                                                                           |
|     [\"Warengruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                                           |
|     [\"Menge\"]{.jsonkey}: [ \... ]{.jsonvalue},                               float (0.0)                                                                      |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                    string                                                                           |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                                           |
|     [\"Einheit\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                           |
|     [\"Kostenstelle\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                    string                                                                           |
|     [\"Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                          string                                                                           |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                           |
|     [\"Ertragskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                        integer                                                                          |
|     [\"EinzelPreisBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"EinzelPreisNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                           |
|     [\"GesamtPreisBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"GesamtPreisNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                           |
|     [\"GesamtGewicht\"]{.jsonkey}: [ \... ]{.jsonvalue},                       float (0.0)                                                                      |
|     [\"OSS_Daten\"]{.jsonkey}: [ { \"OSSDatenItem\": {\...} } ]{.jsonvalue},   [OSSDatenItem](#Parameter_OSSDatenItem){.navlinkcomment}                         |
|     [\"ER_Artikelkennung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},               string, neu ab Version 22.1                                                      |
|     [\"ER_AuftragPosReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string, neu ab Version 22.1                                                      |
|     [\"ER_KontierungHinweis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string, neu ab Version 22.1                                                      |
|     [\"ER_GrundZuAbschlag\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}               string, neu ab Version 22.1                                                      |
|   ---------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|                                                                                                                                                                 |
| }                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufbelegAddItem .anchor}

::: jsonproto
[VerkaufbelegAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
|   --------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                                 |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string, Neu ab 20.0.0                                                                                  |
|     [\"AuftragNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                string                                                                                                 |
|     [\"VerkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                              [VerkaufbelegArt](#Parameter_VerkaufbelegArt){.navlinkcomment}                                         |
|     [\"Entwurf\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                      boolean (true\|false)                                                                                  |
|     [\"EtikettTag\"]{.jsonkey}: [\...]{.jsonvalue},                                                                     [EtikettTags](#Parameter_EtikettTags){.navlinkcomment}                                                 |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                    date (yyyy-mm-dd)                                                                                      |
|     [\"Lieferdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              date (yyyy-mm-dd)                                                                                      |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string                                                                                                 |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                                 |
|     [\"RechnAnschrift\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           string                                                                                                 |
|     [\"LieferAnschrift\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                          string                                                                                                 |
|     [\"LaVerwenden\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                  boolean (true\|false)                                                                                  |
|     [\"Betreff\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                  string                                                                                                 |
|     [\"Anrede\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                   string                                                                                                 |
|     [\"KopfText\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string                                                                                                 |
|     [\"FussText\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string                                                                                                 |
|     [\"Grussformel\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string                                                                                                 |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                  string                                                                                                 |
|     [\"Bearbeiter\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                                 |
|     [\"BearbeiterAngeben\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                            boolean (true\|false)                                                                                  |
|     [\"Steuergebiet\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                 [Steuergebiet](#Parameter_Steuergebiet){.navlinkcomment}                                               |
|     [\"BerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},                                                                  [VerkaufBelegKalkbasis](#Parameter_VerkaufBelegKalkbasis){.navlinkcomment}                             |
|     [\"VKPreisliste_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                          string                                                                                                 |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string                                                                                                 |
|     [\"Zahlungsbedingungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                      string                                                                                                 |
|     [\"SepaMandatReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string                                                                                                 |
|     [\"SepaBankeinzug\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           date (yyyy-mm-dd), Neu ab 18.0.0, optional wenn abweichend von Sepamandat-Vorgabe                      |
|     [\"Lieferart\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                string                                                                                                 |
|     [\"Versandnummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string                                                                                                 |
|     [\"VersandURL\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string, Neu ab 19.0.0                                                                                  |
|     [\"Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                   string                                                                                                 |
|     [\"Lagerbuchung\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                 boolean (true\|false)                                                                                  |
|     [\"VerkaufVorbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string, Wird für Beleg-Weiterleitung benutzt                                                           |
|     [\"AbrZeitraumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           date (yyyy-mm-dd), neu ab Version 22.1                                                                 |
|     [\"AbrZeitraumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           date (yyyy-mm-dd), neu ab Version 22.1                                                                 |
|     [\"ER_ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, neu ab Version 22.1                                                                            |
|     [\"ER_VertragNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, neu ab Version 22.1                                                                            |
|     [\"ER_AuftragNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, neu ab Version 22.1                                                                            |
|     [\"ER_VergabeNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, neu ab Version 22.1                                                                            |
|     [\"ER_Objektkennung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                         string, neu ab Version 22.1                                                                            |
|     [\"ER_Bemerkungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           string, neu ab Version 22.1                                                                            |
|     [\"ER_GrundZuAbschlag\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string, neu ab Version 22.1                                                                            |
|     [\"ER_VorgaengerRechnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                    string, neu ab Version 22.1                                                                            |
|     [\"ER_Verwendungszweck\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                      string, neu ab Version 22.1                                                                            |
|     [\"VerkaufbelegPositionItemList\"]{.jsonkey}: [ { \"VerkaufbelegPositionAddItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [VerkaufbelegPositionAddItem](#Parameter_VerkaufbelegPositionAddItem){.navlinkcomment}   |
|   --------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                                                                                                |
| }                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufbelegPositionAddItem .anchor}

::: jsonproto
[VerkaufbelegPositionAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                              |
|                                                                                                                                                                |
|   --------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|     [\"Nummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                           |
|     [\"PosNrManuell\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                   string                                                                           |
|     [\"VerkaufbelegPositionArt\"]{.jsonkey}: [ \... ]{.jsonvalue},            [VerkaufbelegPositionArt](#Parameter_VerkaufbelegPositionArt){.navlinkcomment}   |
|     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                                           |
|     [\"ArtikelArt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                                           |
|     [\"ArtikelNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                           |
|     [\"Warengruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                    string                                                                           |
|     [\"Menge\"]{.jsonkey}: [ \... ]{.jsonvalue},                              float (0.0)                                                                      |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                   string                                                                           |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                    string                                                                           |
|     [\"Einheit\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                        string                                                                           |
|     [\"Kostenstelle\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                   string                                                                           |
|     [\"Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                         string                                                                           |
|     [\"EinzelPreisBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                                           |
|     [\"EinzelPreisNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"Ertragskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                       integer                                                                          |
|     [\"ER_Artikelkennung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string, neu ab Version 22.1                                                      |
|     [\"ER_AuftragPosReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string, neu ab Version 22.1                                                      |
|     [\"ER_KontierungHinweis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string, neu ab Version 22.1                                                      |
|     [\"ER_GrundZuAbschlag\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string, neu ab Version 22.1                                                      |
|     [\"OSS_Daten\"]{.jsonkey}: [ { \"OSSDatenItem\": {\...} } ]{.jsonvalue}   [OSSDatenItem](#Parameter_OSSDatenItem){.navlinkcomment}                         |
|   --------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|                                                                                                                                                                |
| }                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufbelegPrintItem .anchor}

::: jsonproto
[VerkaufbelegPrintItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------+
| {                                                                                                   |
|                                                                                                     |
|   --------------------------------------------------------- --------------------------------------- |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                  |
|     [\"Dateigroesse\"]{.jsonkey}: [ \... ]{.jsonvalue},     integer                                 |
|     [\"Dateityp\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                  |
|     [\"DatenBASE64\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string, Raw-Daten in BASE64-Kodierung   |
|   --------------------------------------------------------- --------------------------------------- |
|                                                                                                     |
| }                                                                                                   |
+-----------------------------------------------------------------------------------------------------+
:::

\
[]{#verkauf .anchor}\

### Funktionsliste von Verkaufsbelege

[]{#verkauf_verkaufbelegFilterTemplate .anchor}

:::::: memitem
::: memproto
[verkaufbelegFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
Vorlage für Verkaufbeleg-Filter

::: mohelpinfo
\
Dient zur Steuerung von verkaufbelegList.
:::

**Aufruf:**
:   { \"verkaufbelegFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegFilterTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegFilter\": {\...} } ]{.jsonvalue}   [VerkaufbelegFilter](#Parameter_VerkaufbelegFilter){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#verkauf_verkaufbelegList .anchor}

:::::: memitem
::: memproto
[verkaufbelegList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
Auflistung Verkaufbelege

::: mohelpinfo
\
Über einen optionalen Filter kann die Ausgabe von verkaufbelegList gesteuert werden.\
Ablauf:\
1. Datenstruktur VerkaufbelegFilter über verkaufbelegFilterTemplate generieren.\
2. Daten von VerkaufbelegFilter anpassen.\
3. Funktion verkaufbelegList ausführen.\
Ergebnis ist eine Liste der vorhandenen Verkaufbelege.\
Ohne Filterübergabe wird ein Filter mit den Standardwerten verwendet. Als Datumsbereich gilt dann i.d.R. das aktuelle Geschäftsjahr.
:::

**Aufruf:**
:   { \"verkaufbelegList\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |     [\"VerkaufbelegFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [VerkaufbelegFilter](#Parameter_VerkaufbelegFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |                                                                                                                                                  |
    | }                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegListitem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [VerkaufbelegListitem](#Parameter_VerkaufbelegListitem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                         |
    | }                                                                                                                                                                                       |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#verkauf_verkaufbelegGet .anchor}

:::::: memitem
::: memproto
[verkaufbelegGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
Liefert Details eines Verkaufbeleg

::: mohelpinfo
\
Es können Details zu einem Verkaufbeleg abgerufen werden.\
Der Beleg wird durch Verkaufbeleg_ID adressiert.\
Diese kann durch verkaufbelegList ermittelt werden.
:::

**Aufruf:**
:   { \"verkaufbelegGet\":
    +--------------------------------------------------------------------------+
    | {                                                                        |
    |   ------------------------------------------------------------- -------- |
    |     [\"Verkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ------------------------------------------------------------- -------- |
    |                                                                          |
    | }                                                                        |
    +--------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                     |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegItem\": {\...} } ]{.jsonvalue}   [VerkaufbelegItem](#Parameter_VerkaufbelegItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                                       |
    | }                                                                                                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#verkauf_verkaufbelegModify .anchor}

:::::: memitem
::: memproto
[verkaufbelegModify]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
modifiziert vorhandenen, nicht weitergeleiteten Verkaufbeleg

::: mohelpinfo
\
Ablauf:\
1. Struktur VerkaufbelegItem über verkaufbelegGet abrufen.Es wird ein gültiger VersionKey geliefert.\
2. Daten von VerkaufbelegItem bei Bedarf anpassen.\
3. Funktion verkaufbelegModify ausführen.\
Es wird ein Status über Erfolg/Fehler der Operation zurückgeliefert.\
Hinweis: Es sind nicht alle Daten über verkaufbelegModify modifizierbar, sondern nur die, welche nicht als READONLY deklariert sind.\
Bei festgeschriebenen bzw. als gedruckt markierten Belegen können nur noch die Notizen geändert werden.\
Es sollten nur die Parameter übergeben werden, welche auch geändert werden sollen. Alle anderen sollten aus VerkaufbelegItem entfernt werden.\
\
Wird die Zuweisung des Ansprechpartners verändert, sollten die Parameter für Anrede und Rechnungsanschrift als Leerstring übergeben werden. Dann erfolgt eine automatische Anpassung dieser Texte.\
\
Beispielaufruf Änderung Notizen (Verkaufbeleg_ID,VersionKey beispielhaft)\
{\
 \"verkaufbelegModify\":{\
    \"VerkaufbelegItem\":{\
     \"Verkaufbeleg_ID\":\"481A62479DF4207DB23598B6461308\",\
     \"VersionKey\":\"99276D86013D6FE47EFB22572D96B63624\",\
     \"Notizen\":\"Text für Notizen\"\
   }\
  }\
}
:::

**Aufruf:**
:   { \"verkaufbelegModify\":
    +---------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                               |
    |   ---------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"VerkaufbelegItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [VerkaufbelegItem](#Parameter_VerkaufbelegItem){.navlinkcomment}   |
    |   ---------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                 |
    | }                                                                                                                               |
    +---------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegModifyResponse\":
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

[]{#verkauf_verkaufbelegTemplate .anchor}

:::::: memitem
::: memproto
[verkaufbelegTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
liefert VerkaufbelegAddItem als Vorlage

::: mohelpinfo
\
Es wird einen Datenstruktur VerkaufbelegAddItem erzeugt.\
Entsprechend der übergebenen Parameter wird die Datenstruktur vorbelegt.\
Diese Datenstruktur wird für verkaufbelegAdd,verkaufbelegPreview verwendet.\
Zur Ermittelung des Positionspreises wird die Preisliste, welche der Adresse hinterlegt ist, verwendet.\
Optional kann diese durch VKPreisliste_ID überschrieben werden.\
Weitere Hinweise zur Verwendung in diesen Funktionen.
:::

**Aufruf:**
:   { \"verkaufbelegTemplate\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                |
    |   -------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------- |
    |     [\"VerkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue},                                           integer (optional)                                                                          |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                            string (optional)                                                                           |
    |     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                    string (optional)                                                                           |
    |     [\"VKPreisliste_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                       string (optional)                                                                           |
    |     [\"ArtikelAddPostenList\"]{.jsonkey}: [ { \"ArtikelAddPosten\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [ArtikelAddPosten](#Parameter_ArtikelAddPosten){.navlinkcomment} (optional)   |
    |   -------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                  |
    | }                                                                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegAddItem\": {\...} } ]{.jsonvalue}   [VerkaufbelegAddItem](#Parameter_VerkaufbelegAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#verkauf_verkaufbelegDuplikatTemplate .anchor}

:::::: memitem
::: memproto
[verkaufbelegDuplikatTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
Vorlage für einen duplizierten Verkaufbeleg

::: mohelpinfo
\
Es wird einen Datenstruktur VerkaufbelegAddItem erzeugt.\
Entsprechend der übergebenen Parameter wird die Datenstruktur vorbelegt.\
Diese Datenstruktur wird für verkaufbelegAdd,verkaufbelegPreview verwendet.\
Weitere Hinweise zur Verwendung in diesen Funktionen.
:::

**Aufruf:**
:   { \"verkaufbelegDuplikatTemplate\":
    +----------------------------------------------------------------------------------------+
    | {                                                                                      |
    |   ---------------------------------------------------------------- ------------------- |
    |     [\"Verkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string              |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string (optional)   |
    |     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string (optional)   |
    |   ---------------------------------------------------------------- ------------------- |
    |                                                                                        |
    | }                                                                                      |
    +----------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegDuplikatTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegAddItem\": {\...} } ]{.jsonvalue}   [VerkaufbelegAddItem](#Parameter_VerkaufbelegAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#verkauf_verkaufbelegWeiterleitungTemplate .anchor}

:::::: memitem
::: memproto
[verkaufbelegWeiterleitungTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
Vorlage für einen weitergeleiteten Verkaufbeleg

::: mohelpinfo
\
Es wird einen Datenstruktur VerkaufbelegAddItem erzeugt.\
Entsprechend der übergebenen Parameter wird die Datenstruktur vorbelegt.\
Diese Datenstruktur wird für verkaufbelegWeiterleitung,verkaufbelegPreview verwendet.\
Weitere Hinweise zur Verwendung in diesen Funktionen.
:::

**Aufruf:**
:   { \"verkaufbelegWeiterleitungTemplate\":
    +----------------------------------------------------------------------------+
    | {                                                                          |
    |   -------------------------------------------------------------- --------- |
    |     [\"Verkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
    |     [\"VerkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue}        integer   |
    |   -------------------------------------------------------------- --------- |
    |                                                                            |
    | }                                                                          |
    +----------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegWeiterleitungTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegAddItem\": {\...} } ]{.jsonvalue}   [VerkaufbelegAddItem](#Parameter_VerkaufbelegAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#verkauf_verkaufbelegPositionTemplate .anchor}

:::::: memitem
::: memproto
[verkaufbelegPositionTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
liefert VerkaufbelegPositionAddItem als Vorlage

::: mohelpinfo
\
Es wird einen Datenstruktur VerkaufbelegPositionAddItem erzeugt.\
Entsprechend der übergebenen Parameter wird die Datenstruktur vorbelegt.\
Diese Datenstruktur kann zur Ergänzung von VerkaufbelegAddItem verwendet werden.\
Zur Ermittelung des Positionspreises wird die Preisliste, welche der Adresse hinterlegt ist, verwendet.\
Optional kann diese durch VKPreisliste_ID überschrieben werden.\
Weitere Hinweise zur Verwendung in diesen Funktionen.
:::

**Aufruf:**
:   { \"verkaufbelegPositionTemplate\":
    +---------------------------------------------------------------------------------------+
    | {                                                                                     |
    |   -------------------------------------------------------------- -------------------- |
    |     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string (optional)    |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string (optional)    |
    |     [\"VKPreisliste_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string (optional)    |
    |     [\"Artikelmenge\"]{.jsonkey}: [ \... ]{.jsonvalue}           integer (optional)   |
    |   -------------------------------------------------------------- -------------------- |
    |                                                                                       |
    | }                                                                                     |
    +---------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegPositionTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                      |
    |   ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegPositionAddItem\": {\...} } ]{.jsonvalue}   [VerkaufbelegPositionAddItem](#Parameter_VerkaufbelegPositionAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                        |
    | }                                                                                                                                                                                      |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#verkauf_verkaufbelegPreview .anchor}

:::::: memitem
::: memproto
[verkaufbelegPreview]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
berechnet einen Verkaufbeleg ohne ihn zu sichern

::: mohelpinfo
\
Diese Funktion wird für interaktive Clients verwendet um eine Voransicht eines anzulegenden Belegs zu erzeugen.\
Ablauf:\
1. Datenstruktur VerkaufbelegAddItem über verkaufbelegTemplate, verkaufbelegDuplikatTemplate oder verkaufbelegWeiterleitungTemplate generieren.\
2. Daten von VerkaufbelegAddItem bei Bedarf anpassen.\
3. Funktion verkaufbelegPreview ausführen.\
Ergebnis ist eine Datenstruktur VerkaufbelegItem welche einem angelegten Verkaufbeleg entspricht.
:::

**Aufruf:**
:   { \"verkaufbelegPreview\":
    +------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                        |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"VerkaufbelegAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [VerkaufbelegAddItem](#Parameter_VerkaufbelegAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                          |
    | }                                                                                                                                        |
    +------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegPreviewResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                     |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegItem\": {\...} } ]{.jsonvalue}   [VerkaufbelegItem](#Parameter_VerkaufbelegItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                                       |
    | }                                                                                                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#verkauf_verkaufbelegAdd .anchor}

:::::: memitem
::: memproto
[verkaufbelegAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
fügt einen neuen Verkaufbeleg hinzu

::: mohelpinfo
\
Ablauf:\
1. Datenstruktur VerkaufbelegAddItem über verkaufbelegTemplate oder verkaufbelegDuplikatTemplate generieren.\
2. Daten von VerkaufbelegAddItem anpassen.\
3. Funktion verkaufbelegAdd ausführen.\
Es wird ein Verkaufbeleg angelegt. Bei Erfolg werden Statuscode=0 und eine Insert_ID zurückgeliefert.\
Ein Fehler liefert Statuscode \<\> 0 und Infos zum aufgetretenen Problem.\
\
Ab Version 18.4 wird das One Stop Shop - Verfahren (OSS) unterstützt. Voraussetzung ist, das dem Erlöskonto ein OSS-Steuersatz zugewiesen wurde.\
Bei Verwendung eines solchen Erlöskontos können den Belegpositionen landesspezifische Steuerdaten zugewiesen werden.
:::

**Aufruf:**
:   { \"verkaufbelegAdd\":
    +------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                        |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"VerkaufbelegAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [VerkaufbelegAddItem](#Parameter_VerkaufbelegAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                          |
    | }                                                                                                                                        |
    +------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegAddResponse\":
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

[]{#verkauf_verkaufbelegWeiterleitung .anchor}

:::::: memitem
::: memproto
[verkaufbelegWeiterleitung]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
fügt einen Verkaufbeleg als Weiterleitung hinzu

::: mohelpinfo
\
Ablauf:\
1. Datenstruktur VerkaufbelegAddItem über verkaufbelegWeiterleitungTemplate generieren.\
2. Daten von VerkaufbelegAddItem bei Bedarf anpassen (VerkaufVorbeleg_ID darf nicht geändert werden).\
3. Funktion verkaufbelegWeiterleitung ausführen.\
Es wird ein Verkaufbeleg angelegt. Bei Erfolg werden Statuscode=0 und eine Insert_ID zurückgeliefert.\
Bei einem Fehler wird Statuscode \<\> 0 und weitere Infos zum aufgetretenen Fehler geliefert.
:::

**Aufruf:**
:   { \"verkaufbelegWeiterleitung\":
    +------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                        |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"VerkaufbelegAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [VerkaufbelegAddItem](#Parameter_VerkaufbelegAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                          |
    | }                                                                                                                                        |
    +------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegWeiterleitungResponse\":
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

[]{#verkauf_verkaufbelegDelete .anchor}

:::::: memitem
::: memproto
[verkaufbelegDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
löscht einen Verkaufbeleg

::: mohelpinfo
\
Es wird ein Verkaufbeleg gelöscht.\
Der Beleg wird durch Verkaufbeleg_ID adressiert.\
Diese kann durch verkaufbelegList ermittelt werden.
:::

**Aufruf:**
:   { \"verkaufbelegDelete\":
    +--------------------------------------------------------------------------+
    | {                                                                        |
    |   ------------------------------------------------------------- -------- |
    |     [\"Verkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ------------------------------------------------------------- -------- |
    |                                                                          |
    | }                                                                        |
    +--------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegDeleteResponse\":
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

[]{#verkauf_verkaufbelegAddAttachment .anchor}

:::::: memitem
::: memproto
[verkaufbelegAddAttachment]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
fügt ein Attachment einem Verkaufbeleg hinzu

::: mohelpinfo
\
An den Verkaufbeleg wird ein Dokument oder Link als Attachment angefügt.\
Ablauf:\
1. Den Beleg durch Verkaufbeleg_ID festlegen.\
2. Datenstruktur AttachmentAddItem mit Daten füllen. Es kann entweder DatenBASE64 oder Link gesetzt werden. Die Dokument-Daten DatenBASE64 müssen als Base64 codiert übergeben werden.\
3. Funktion verkaufbelegAddAttachment ausführen.\
Bei Erfolg werden Statuscode=0 und eine Insert_ID vom Typ Attachment_ID zurückgeliefert.\
Bei einem Fehler wird Statuscode \<\> 0 und weitere Infos zum aufgetretenen Fehler geliefert.\
Die Verwaltung der Attachments erfolgt im Modul Attachment-Verwaltung.
:::

**Aufruf:**
:   { \"verkaufbelegAddAttachment\":
    +---------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                     |
    |   -------------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"Verkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                               |
    |     [\"AttachmentAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}      [AttachmentAddItem](#Parameter_AttachmentAddItem){.navlinkcomment}   |
    |   -------------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                       |
    | }                                                                                                                                     |
    +---------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegAddAttachmentResponse\":
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

[]{#verkauf_verkaufbelegPrintPDF .anchor}

:::::: memitem
::: memproto
[verkaufbelegPrintPDF]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
liefert einen Verkaufbeleg als PDF

::: mohelpinfo
\
Für einen Verkaufbeleg wird ein PDF generiert.\
Ablauf:\
1. Den Beleg durch Verkaufbeleg_ID festlegen.\
2. Über DruckformularName das gewünschte Druckformular festlegen.\
3. Festlegen ob der Beleg nach erfolgreicher PDF-Ausgabe als gedruckt markiert werden soll .\
4. Funktion verkaufbelegPrintPDF ausführen.\
Bei Erfolg wird eine Datenstruktur vom Typ VerkaufbelegPrintItem zurückgeliefert, diese enthält das PDF in Base64-Kodierung.\
:::

**Aufruf:**
:   { \"verkaufbelegPrintPDF\":
    +--------------------------------------------------------------------------------------------+
    | {                                                                                          |
    |   ---------------------------------------------------------------- ----------------------- |
    |     [\"Verkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                  |
    |     [\"DruckformularName\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                  |
    |     [\"MarkAsPrinted\"]{.jsonkey}: [ \... ]{.jsonvalue}            boolean (true\|false)   |
    |   ---------------------------------------------------------------- ----------------------- |
    |                                                                                            |
    | }                                                                                          |
    +--------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"verkaufbelegPrintPDFResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                    |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufbelegPrintItem\": {\...} } ]{.jsonvalue}   [VerkaufbelegPrintItem](#Parameter_VerkaufbelegPrintItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |                                                                                                                                                                      |
    | }                                                                                                                                                                    |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#Content_einkauf .anchor}  \

