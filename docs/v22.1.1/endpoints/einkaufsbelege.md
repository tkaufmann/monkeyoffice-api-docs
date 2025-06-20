## Einkaufsbelege

[]{#einkauf_Datenstrukturen .anchor}

### Datenstrukturen von Einkaufsbelege

[]{#Parameter_EinkaufbelegArt .anchor}

::: jsonproto
[EinkaufbelegArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| { [\"EinkaufbelegArt\"]{.jsonkey tag="EinkaufbelegArt"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------------------------------- |
|                                                                               |   Aufzählung, Integer                 101=[Bestellanfrage]{tag="Bestellanfrage"}\                 |
|                                                                               |                                       102=[Bestellung]{tag="Bestellung"}\                         |
|                                                                               |                                       103=[Wareneingang]{tag="Wareneingang"}\                     |
|                                                                               |                                       104=[Eingangsrechnung]{tag="Eingangsrechnung"}\             |
|                                                                               |                                       105=[Lieferantengutschrift]{tag="Lieferantengutschrift"}\   |
|                                                                               |                                       106=[Rücksendung]{tag="Rücksendung"}\                       |
|                                                                               |                                       107=[Stornierung]{tag="Stornierung"}                        |
|                                                                               |                                                                                                   |
|                                                                               |   ----------------------------------- ----------------------------------------------------------- |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegStatus .anchor}

::: jsonproto
[EinkaufbelegStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| { [\"EinkaufbelegStatus\"]{.jsonkey tag="EinkaufbelegStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------------------- |
|                                                                                     |   Aufzählung, Integer                 1=[Alle]{tag="Alle"}\                                    |
|                                                                                     |                                       2=[Nur Dokumente]{tag="Nur Dokumente"}\                  |
|                                                                                     |                                       3=[Nur Entwürfe/Vorlagen]{tag="Nur Entwürfe/Vorlagen"}   |
|                                                                                     |                                                                                                |
|                                                                                     |   ----------------------------------- -------------------------------------------------------- |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegDruckstatus .anchor}

::: jsonproto
[EinkaufbelegDruckstatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| { [\"EinkaufbelegDruckstatus\"]{.jsonkey tag="EinkaufbelegDruckstatus"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------------- |
|                                                                                               |   Aufzählung, Integer                 0=[Alle]{tag="Alle"}\                         |
|                                                                                               |                                       1=[nur ungedruckte]{tag="nur ungedruckte"}\   |
|                                                                                               |                                       2=[nur gedruckte]{tag="nur gedruckte"}        |
|                                                                                               |                                                                                     |
|                                                                                               |   ----------------------------------- --------------------------------------------- |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufBelegKalkbasis .anchor}

::: jsonproto
[EinkaufBelegKalkbasis]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"EinkaufBelegKalkbasis\"]{.jsonkey tag="EinkaufBelegKalkbasis"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                           |   Aufzählung, Integer                 0=[Netto]{tag="Netto"}\             |
|                                                                                           |                                       1=[Brutto]{tag="Brutto"}            |
|                                                                                           |                                                                           |
|                                                                                           |   ----------------------------------- ----------------------------------- |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegPositionArt .anchor}

::: jsonproto
[EinkaufbelegPositionArt]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| { [\"EinkaufbelegPositionArt\"]{.jsonkey tag="EinkaufbelegPositionArt"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------------------------------------------- |
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
[]{#Parameter_EinkaufbelegFilter .anchor}

::: jsonproto
[EinkaufbelegFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
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
|     [\"Bestellanfrage\"]{.jsonkey}: [ \... ]{.jsonvalue},            boolean (true\|false)                                                                                        |
|     [\"Bestellung\"]{.jsonkey}: [ \... ]{.jsonvalue},                boolean (true\|false)                                                                                        |
|     [\"Wareneingang\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"Ruecksendung\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                                                                        |
|     [\"Eingangsrechnung\"]{.jsonkey}: [ \... ]{.jsonvalue},          boolean (true\|false)                                                                                        |
|     [\"Lieferantengutschrift\"]{.jsonkey}: [ \... ]{.jsonvalue},     boolean (true\|false)                                                                                        |
|     [\"Storno\"]{.jsonkey}: [ \... ]{.jsonvalue},                    boolean (true\|false)                                                                                        |
|     [\"EinkaufbelegStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},        [EinkaufbelegStatus](#Parameter_EinkaufbelegStatus){.navlinkcomment}                                         |
|     [\"EinkaufbelegDruckstatus\"]{.jsonkey}: [ \... ]{.jsonvalue},   [EinkaufbelegDruckstatus](#Parameter_EinkaufbelegDruckstatus){.navlinkcomment}                               |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},         [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}                                           |
|     [\"BestellNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                                                       |
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
|     [\"FolgebelegStatus\"]{.jsonkey}: []{.jsonvalue}                 [EinkaufFolgebelegStatus](#Parameter_EinkaufFolgebelegStatus){.navlinkcomment}, Neu ab 18.3                  |
|   ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                                                   |
| }                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegListitem .anchor}

::: jsonproto
[EinkaufbelegListitem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                 |
|                                                                                                                                   |
|   -------------------------------------------------------------- ---------------------------------------------------------------- |
|     [\"Einkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                           |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                           |
|     [\"BestellNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                           |
|     [\"EinkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue},       [EinkaufbelegArt](#Parameter_EinkaufbelegArt){.navlinkcomment}   |
|     [\"Kunde\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                           |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             date (yyyy-mm-dd)                                                |
|     [\"Lieferdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       date (yyyy-mm-dd)                                                |
|     [\"GesamtNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                           |
|     [\"GesamtBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                           |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                           |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}          string                                                           |
|   -------------------------------------------------------------- ---------------------------------------------------------------- |
|                                                                                                                                   |
| }                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegItem .anchor}

::: jsonproto
[EinkaufbelegItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                 |
|   ------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------- |
|     [\"Einkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string, readonly                                                                                           |
|     [\"VersionKey\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string, readonly                                                                                           |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string, readonly                                                                                           |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                    string, Neu ab 20.0.0                                                                                      |
|     [\"BestellNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, readonly                                                                                           |
|     [\"EinkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                           [EinkaufbelegArt](#Parameter_EinkaufbelegArt){.navlinkcomment}, readonly                                   |
|     [\"Kunde\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string, readonly                                                                                           |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 date (yyyy-mm-dd), readonly                                                                                |
|     [\"Lieferdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                           date (yyyy-mm-dd), readonly                                                                                |
|     [\"GesamtNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                         string, readonly                                                                                           |
|     [\"GesamtBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"Projekt_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string, readonly                                                                                           |
|     [\"ProjektNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string, readonly                                                                                           |
|     [\"Entwurf\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                   boolean (true\|false), readonly                                                                            |
|     [\"EtikettTag\"]{.jsonkey}: [\...]{.jsonvalue},                                                                  [EtikettTags](#Parameter_EtikettTags){.navlinkcomment}, ab 19.2.1 nicht mehr readonly                      |
|     [\"Zahlungstatus\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                             [Zahlungstatus](#Parameter_Zahlungstatus){.navlinkcomment}, readonly                                       |
|     [\"FestschreibStatus\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                         [FestschreibStatus](#Parameter_FestschreibStatus){.navlinkcomment}, readonly                               |
|     [\"LieferNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string, readonly, veraltet ab 16.0.1, entfällt ab 17.0.0                                                   |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string, readonly, Neu ab 16.0.1, (überschreibt LieferNr)                                                   |
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
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              string, readonly                                                                                           |
|     [\"Steuergebiet\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                              [Steuergebiet](#Parameter_Steuergebiet){.navlinkcomment}, readonly                                         |
|     [\"GesamtRabattFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"GesamtSteuerFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"GesamtRabattSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"GesamtSteuerSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                        string, readonly                                                                                           |
|     [\"Zahlungsbedingungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                   string, readonly                                                                                           |
|     [\"Lieferart\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                             string                                                                                                     |
|     [\"Versandnummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                         string                                                                                                     |
|     [\"VersandURL\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string, Neu ab 19.0.0                                                                                      |
|     [\"Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                string, readonly                                                                                           |
|     [\"VorbelegIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},                                                        Array vom Typ string, readonly                                                                             |
|     [\"AttachmentIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},                                                      Array vom Typ string, readonly                                                                             |
|     [\"EinkaufbelegPositionItemList\"]{.jsonkey}: [ { \"EinkaufbelegPositionItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [EinkaufbelegPositionItem](#Parameter_EinkaufbelegPositionItem){.navlinkcomment}, readonly   |
|   ------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                 |
| }                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegPositionItem .anchor}

::: jsonproto
[EinkaufbelegPositionItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                        |
|                                                                                                                                                          |
|   --------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|     [\"Nummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                   string                                                                           |
|     [\"PosNrManuell\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"EinkaufbelegPositionArt\"]{.jsonkey}: [ \... ]{.jsonvalue},      [EinkaufbelegPositionArt](#Parameter_EinkaufbelegPositionArt){.navlinkcomment}   |
|     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},               string                                                                           |
|     [\"ArtikelArt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},               string                                                                           |
|     [\"ArtikelNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                           |
|     [\"Warengruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                           |
|     [\"Menge\"]{.jsonkey}: [ \... ]{.jsonvalue},                        float (0.0)                                                                      |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                           |
|     [\"Einheit\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                                           |
|     [\"Kostenstelle\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                   string                                                                           |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},               string                                                                           |
|     [\"Aufwandskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                integer                                                                          |
|     [\"EinzelPreisBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                           |
|     [\"EinzelPreisNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                           |
|     [\"GesamtPreisBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                           |
|     [\"GesamtPreisNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                           |
|     [\"EinzelPreisNettoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                           |
|     [\"EinzelPreisBruttoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                           |
|     [\"GesamtPreisBruttoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                           |
|     [\"GesamtPreisNettoSW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                           |
|     [\"GesamtGewicht\"]{.jsonkey}: [ \... ]{.jsonvalue},                float (0.0)                                                                      |
|     [\"VorbelegBestellNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string, Neu ab 20.1.0                                                            |
|     [\"VorbelegEinkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string, Neu ab 20.1.0                                                            |
|   --------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|                                                                                                                                                          |
| }                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegAddItem .anchor}

::: jsonproto
[EinkaufbelegAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
|   --------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ |
|     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string                                                                                                 |
|     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string, Neu ab 20.0.0                                                                                  |
|     [\"BestellNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                string                                                                                                 |
|     [\"EinkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                              [EinkaufbelegArt](#Parameter_EinkaufbelegArt){.navlinkcomment}                                         |
|     [\"Entwurf\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                      boolean (true\|false)                                                                                  |
|     [\"EtikettTag\"]{.jsonkey}: [\...]{.jsonvalue},                                                                     [EtikettTags](#Parameter_EtikettTags){.navlinkcomment}                                                 |
|     [\"Datum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                    date (yyyy-mm-dd)                                                                                      |
|     [\"Lieferdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                              date (yyyy-mm-dd)                                                                                      |
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
|     [\"BearbeiterAngeben\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                            boolean (true\|false), Neu ab 17.0.0                                                                   |
|     [\"Waehrung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string                                                                                                 |
|     [\"Steuergebiet\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                 [Steuergebiet](#Parameter_Steuergebiet){.navlinkcomment}                                               |
|     [\"BerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},                                                                  [EinkaufBelegKalkbasis](#Parameter_EinkaufBelegKalkbasis){.navlinkcomment}                             |
|     [\"Zahlungsbedingungen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                      string                                                                                                 |
|     [\"Lieferart\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                string                                                                                                 |
|     [\"Versandnummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                            string                                                                                                 |
|     [\"VersandURL\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                               string, Neu ab 19.0.0                                                                                  |
|     [\"Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                   string                                                                                                 |
|     [\"LieferNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string, veraltet ab 16.0.1, entfällt ab 17.0.0                                                         |
|     [\"Referenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                                 string, Neu ab 16.0.1, (überschreibt LieferNr)                                                         |
|     [\"Lagerbuchung\"]{.jsonkey}: [ \... ]{.jsonvalue},                                                                 boolean (true\|false)                                                                                  |
|     [\"EinkaufVorbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                                       string, Benutzung für Weiterleitung, nicht ändern                                                      |
|     [\"EinkaufbelegPositionItemList\"]{.jsonkey}: [ { \"EinkaufbelegPositionAddItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [EinkaufbelegPositionAddItem](#Parameter_EinkaufbelegPositionAddItem){.navlinkcomment}   |
|   --------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------ |
|                                                                                                                                                                                                                                |
| }                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegPositionAddItem .anchor}

::: jsonproto
[EinkaufbelegPositionAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                           |
|                                                                                                                                                             |
|   ------------------------------------------------------------------------ -------------------------------------------------------------------------------- |
|     [\"Nummer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                           |
|     [\"PosNrManuell\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                           |
|     [\"EinkaufbelegPositionArt\"]{.jsonkey}: [ \... ]{.jsonvalue},         [EinkaufbelegPositionArt](#Parameter_EinkaufbelegPositionArt){.navlinkcomment}   |
|     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                                           |
|     [\"ArtikelArt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                                           |
|     [\"ArtikelNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                   string                                                                           |
|     [\"Warengruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                 string                                                                           |
|     [\"Menge\"]{.jsonkey}: [ \... ]{.jsonvalue},                           float (0.0)                                                                      |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                           |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                 string                                                                           |
|     [\"Einheit\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                     string                                                                           |
|     [\"Kostenstelle\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                           |
|     [\"Rabatt\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                      string                                                                           |
|     [\"EinzelPreisBruttoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                                           |
|     [\"EinzelPreisNettoFW\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                           |
|     [\"Aufwandskonto\"]{.jsonkey}: [ \... ]{.jsonvalue},                   integer                                                                          |
|     [\"EinkaufVorbelegPosition_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string, Wird für Weiterleitung verwendet, nicht ändern                           |
|   ------------------------------------------------------------------------ -------------------------------------------------------------------------------- |
|                                                                                                                                                             |
| }                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EinkaufbelegPrintItem .anchor}

::: jsonproto
[EinkaufbelegPrintItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
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
[]{#einkauf .anchor}\

### Funktionsliste von Einkaufsbelege

[]{#einkauf_einkaufbelegFilterTemplate .anchor}

::::: memitem
::: memproto
[einkaufbelegFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Einkaufbeleg-Filter

**Aufruf:**
:   { \"einkaufbelegFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegFilterTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegFilter\": {\...} } ]{.jsonvalue}   [EinkaufbelegFilter](#Parameter_EinkaufbelegFilter){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#einkauf_einkaufbelegList .anchor}

::::: memitem
::: memproto
[einkaufbelegList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung Einkaufbelege

**Aufruf:**
:   { \"einkaufbelegList\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |     [\"EinkaufbelegFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [EinkaufbelegFilter](#Parameter_EinkaufbelegFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |                                                                                                                                                  |
    | }                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegListitem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [EinkaufbelegListitem](#Parameter_EinkaufbelegListitem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                         |
    | }                                                                                                                                                                                       |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#einkauf_einkaufbelegGet .anchor}

::::: memitem
::: memproto
[einkaufbelegGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details eines Einkaufbeleg

**Aufruf:**
:   { \"einkaufbelegGet\":
    +--------------------------------------------------------------------------+
    | {                                                                        |
    |   ------------------------------------------------------------- -------- |
    |     [\"Einkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ------------------------------------------------------------- -------- |
    |                                                                          |
    | }                                                                        |
    +--------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                     |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegItem\": {\...} } ]{.jsonvalue}   [EinkaufbelegItem](#Parameter_EinkaufbelegItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                                       |
    | }                                                                                                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#einkauf_einkaufbelegModify .anchor}

::::: memitem
::: memproto
[einkaufbelegModify]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
modifiziert vorhandenen, nicht weitergeleiteten Einkaufbeleg

**Aufruf:**
:   { \"einkaufbelegModify\":
    +---------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                               |
    |   ---------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"EinkaufbelegItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [EinkaufbelegItem](#Parameter_EinkaufbelegItem){.navlinkcomment}   |
    |   ---------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                 |
    | }                                                                                                                               |
    +---------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegModifyResponse\":
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

[]{#einkauf_einkaufbelegTemplate .anchor}

::::: memitem
::: memproto
[einkaufbelegTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert EinkaufbelegAddItem als Vorlage

**Aufruf:**
:   { \"einkaufbelegTemplate\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                |
    |   -------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------- |
    |     [\"EinkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue},                                           integer (optional)                                                                          |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                            string (optional)                                                                           |
    |     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                                    string (optional)                                                                           |
    |     [\"ArtikelAddPostenList\"]{.jsonkey}: [ { \"ArtikelAddPosten\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [ArtikelAddPosten](#Parameter_ArtikelAddPosten){.navlinkcomment} (optional)   |
    |   -------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                  |
    | }                                                                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegAddItem\": {\...} } ]{.jsonvalue}   [EinkaufbelegAddItem](#Parameter_EinkaufbelegAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#einkauf_einkaufbelegDuplikatTemplate .anchor}

::::: memitem
::: memproto
[einkaufbelegDuplikatTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für einen duplizierten Einkaufbeleg

**Aufruf:**
:   { \"einkaufbelegDuplikatTemplate\":
    +----------------------------------------------------------------------------------------+
    | {                                                                                      |
    |   ---------------------------------------------------------------- ------------------- |
    |     [\"Einkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string              |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string (optional)   |
    |     [\"Ansprechpartner_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string (optional)   |
    |   ---------------------------------------------------------------- ------------------- |
    |                                                                                        |
    | }                                                                                      |
    +----------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegDuplikatTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegAddItem\": {\...} } ]{.jsonvalue}   [EinkaufbelegAddItem](#Parameter_EinkaufbelegAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#einkauf_einkaufbelegWeiterleitungTemplate .anchor}

::::: memitem
::: memproto
[einkaufbelegWeiterleitungTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für einen weitergeleiteten Einkaufbeleg

**Aufruf:**
:   { \"einkaufbelegWeiterleitungTemplate\":
    +----------------------------------------------------------------------------+
    | {                                                                          |
    |   -------------------------------------------------------------- --------- |
    |     [\"Einkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
    |     [\"EinkaufbelegArt\"]{.jsonkey}: [ \... ]{.jsonvalue}        integer   |
    |   -------------------------------------------------------------- --------- |
    |                                                                            |
    | }                                                                          |
    +----------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegWeiterleitungTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegAddItem\": {\...} } ]{.jsonvalue}   [EinkaufbelegAddItem](#Parameter_EinkaufbelegAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#einkauf_einkaufbelegPositionTemplate .anchor}

::::: memitem
::: memproto
[einkaufbelegPositionTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert EinkaufbelegPositionAddItem als Vorlage

**Aufruf:**
:   { \"einkaufbelegPositionTemplate\":
    +----------------------------------------------------------------------------------+
    | {                                                                                |
    |   --------------------------------------------------------- -------------------- |
    |     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string (optional)    |
    |     [\"Adresse_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string (optional)    |
    |     [\"Artikelmenge\"]{.jsonkey}: [ \... ]{.jsonvalue}      integer (optional)   |
    |   --------------------------------------------------------- -------------------- |
    |                                                                                  |
    | }                                                                                |
    +----------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegPositionTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                      |
    |   ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegPositionAddItem\": {\...} } ]{.jsonvalue}   [EinkaufbelegPositionAddItem](#Parameter_EinkaufbelegPositionAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                        |
    | }                                                                                                                                                                                      |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#einkauf_einkaufbelegPreview .anchor}

::::: memitem
::: memproto
[einkaufbelegPreview]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
berechnet einen Einkaufbeleg ohne zu sichern

**Aufruf:**
:   { \"einkaufbelegPreview\":
    +------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                        |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"EinkaufbelegAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [EinkaufbelegAddItem](#Parameter_EinkaufbelegAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                          |
    | }                                                                                                                                        |
    +------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegPreviewResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                     |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegItem\": {\...} } ]{.jsonvalue}   [EinkaufbelegItem](#Parameter_EinkaufbelegItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                                       |
    | }                                                                                                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#einkauf_einkaufbelegAdd .anchor}

::::: memitem
::: memproto
[einkaufbelegAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt einen neuen Einkaufbeleg hinzu

**Aufruf:**
:   { \"einkaufbelegAdd\":
    +------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                        |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"EinkaufbelegAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [EinkaufbelegAddItem](#Parameter_EinkaufbelegAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                          |
    | }                                                                                                                                        |
    +------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegAddResponse\":
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

[]{#einkauf_einkaufbelegWeiterleitung .anchor}

::::: memitem
::: memproto
[einkaufbelegWeiterleitung]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt einen weitergeleiteten Einkaufbeleg hinzu

**Aufruf:**
:   { \"einkaufbelegWeiterleitung\":
    +------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                        |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"EinkaufbelegAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [EinkaufbelegAddItem](#Parameter_EinkaufbelegAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                          |
    | }                                                                                                                                        |
    +------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegWeiterleitungResponse\":
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

[]{#einkauf_einkaufbelegDelete .anchor}

::::: memitem
::: memproto
[einkaufbelegDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht einen Einkaufbeleg

**Aufruf:**
:   { \"einkaufbelegDelete\":
    +--------------------------------------------------------------------------+
    | {                                                                        |
    |   ------------------------------------------------------------- -------- |
    |     [\"Einkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ------------------------------------------------------------- -------- |
    |                                                                          |
    | }                                                                        |
    +--------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegDeleteResponse\":
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

[]{#einkauf_einkaufbelegAddAttachment .anchor}

::::: memitem
::: memproto
[einkaufbelegAddAttachment]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt ein Attachment einem Einkaufbeleg hinzu

**Aufruf:**
:   { \"einkaufbelegAddAttachment\":
    +---------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                     |
    |   -------------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"Einkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                               |
    |     [\"AttachmentAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}      [AttachmentAddItem](#Parameter_AttachmentAddItem){.navlinkcomment}   |
    |   -------------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                       |
    | }                                                                                                                                     |
    +---------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegAddAttachmentResponse\":
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

[]{#einkauf_einkaufbelegPrintPDF .anchor}

::::: memitem
::: memproto
[einkaufbelegPrintPDF]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert einen Einkaufbeleg als PDF

**Aufruf:**
:   { \"einkaufbelegPrintPDF\":
    +--------------------------------------------------------------------------------------------+
    | {                                                                                          |
    |   ---------------------------------------------------------------- ----------------------- |
    |     [\"Einkaufbeleg_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                  |
    |     [\"DruckformularName\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                  |
    |     [\"MarkAsPrinted\"]{.jsonkey}: [ \... ]{.jsonvalue}            boolean (true\|false)   |
    |   ---------------------------------------------------------------- ----------------------- |
    |                                                                                            |
    | }                                                                                          |
    +--------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"einkaufbelegPrintPDFResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                    |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"EinkaufbelegPrintItem\": {\...} } ]{.jsonvalue}   [EinkaufbelegPrintItem](#Parameter_EinkaufbelegPrintItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------- |
    |                                                                                                                                                                      |
    | }                                                                                                                                                                    |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#Content_buchungen .anchor}  \

