## Artikel und Leistungen

[]{#artikel_Datenstrukturen .anchor}

### Datenstrukturen von Artikel und Leistungen

[]{#Parameter_StueckListeTyp .anchor}

::: jsonproto
[StueckListeTyp]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| { [\"StueckListeTyp\"]{.jsonkey tag="StueckListeTyp"}: [\...]{.jsonvalue} } |   ----------------------------------- ------------------------------------------------- |
|                                                                             |   Aufzählung, Integer                 0=[kein Stückliste]{tag="kein Stückliste"}\       |
|                                                                             |                                       1=[Fertigungsartikel]{tag="Fertigungsartikel"}\   |
|                                                                             |                                       2=[Artikelset]{tag="Artikelset"}                  |
|                                                                             |                                                                                         |
|                                                                             |   ----------------------------------- ------------------------------------------------- |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_Artikelkalkaufwand .anchor}

::: jsonproto
[Artikelkalkaufwand]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"Artikelkalkaufwand\"]{.jsonkey tag="Artikelkalkaufwand"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                     |   Aufzählung, Integer                 1=[Betrag]{tag="Betrag"}\           |
|                                                                                     |                                       2=[Prozent]{tag="Prozent"}          |
|                                                                                     |                                                                           |
|                                                                                     |   ----------------------------------- ----------------------------------- |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_Artikelkalkbasis .anchor}

::: jsonproto
[Artikelkalkbasis]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"Artikelkalkbasis\"]{.jsonkey tag="Artikelkalkbasis"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                 |   Aufzählung, Integer                 1=[Netto]{tag="Netto"}\             |
|                                                                                 |                                       2=[Brutto]{tag="Brutto"}            |
|                                                                                 |                                                                           |
|                                                                                 |   ----------------------------------- ----------------------------------- |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_Artikelkalkmarge .anchor}

::: jsonproto
[Artikelkalkmarge]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"Artikelkalkmarge\"]{.jsonkey tag="Artikelkalkmarge"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                 |   Aufzählung, Integer                 1=[Betrag]{tag="Betrag"}\           |
|                                                                                 |                                       2=[Prozent]{tag="Prozent"}\         |
|                                                                                 |                                       3=[VKGesamt]{tag="VKGesamt"}        |
|                                                                                 |                                                                           |
|                                                                                 |   ----------------------------------- ----------------------------------- |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_Artikelpreis .anchor}

::: jsonproto
[Artikelpreis]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"Artikelpreis\"]{.jsonkey tag="Artikelpreis"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                         |   Aufzählung, Integer                 0=[Netto]{tag="Netto"}\             |
|                                                                         |                                       1=[Brutto]{tag="Brutto"}            |
|                                                                         |                                                                           |
|                                                                         |   ----------------------------------- ----------------------------------- |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_Artikelart .anchor}

::: jsonproto
[Artikelart]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"Artikelart\"]{.jsonkey tag="Artikelart"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                     |   Aufzählung, Integer                 1=[Artikel]{tag="Artikel"}\         |
|                                                                     |                                       2=[Leistung]{tag="Leistung"}        |
|                                                                     |                                                                           |
|                                                                     |   ----------------------------------- ----------------------------------- |
+---------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_Artikelstatus .anchor}

::: jsonproto
[Artikelstatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| { [\"Artikelstatus\"]{.jsonkey tag="Artikelstatus"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------------------------- |
|                                                                           |   Aufzählung, Integer                 0=[Verkauf und Einkauf]{tag="Verkauf und Einkauf"}\   |
|                                                                           |                                       1=[Einkauf]{tag="Einkauf"}\                           |
|                                                                           |                                       2=[Verkauf]{tag="Verkauf"}\                           |
|                                                                           |                                       3=[kein Status]{tag="kein Status"}                    |
|                                                                           |                                                                                             |
|                                                                           |   ----------------------------------- ----------------------------------------------------- |
+---------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_Warengruppeart .anchor}

::: jsonproto
[Warengruppeart]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| { [\"Warengruppeart\"]{.jsonkey tag="Warengruppeart"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------- |
|                                                                             |   Aufzählung, Integer                 1=[Artikelgruppe]{tag="Artikelgruppe"}\      |
|                                                                             |                                       2=[Leistungsgruppe]{tag="Leistungsgruppe"}   |
|                                                                             |                                                                                    |
|                                                                             |   ----------------------------------- -------------------------------------------- |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_WarengruppeListItem .anchor}

::: jsonproto
[WarengruppeListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                              |
|                                                                                                                                |
|   ------------------------------------------------------------- -------------------------------------------------------------- |
|     [\"Warengruppe_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                         |
|     [\"WarengruppeArt\"]{.jsonkey}: [ \... ]{.jsonvalue},       [Warengruppeart](#Parameter_Warengruppeart){.navlinkcomment}   |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                         |
|     [\"Obergruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                         |
|     [\"Obergruppe_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}     string                                                         |
|   ------------------------------------------------------------- -------------------------------------------------------------- |
|                                                                                                                                |
| }                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_WarengruppeItem .anchor}

::: jsonproto
[WarengruppeItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                               |
|                                                                                                                                 |
|   -------------------------------------------------------------- -------------------------------------------------------------- |
|     [\"Warengruppe_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                         |
|     [\"WarengruppeArt\"]{.jsonkey}: [ \... ]{.jsonvalue},        [Warengruppeart](#Parameter_Warengruppeart){.navlinkcomment}   |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                         |
|     [\"Obergruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                         |
|     [\"Obergruppe_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                         |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                         |
|     [\"EKontoInland\"]{.jsonkey}: [ \... ]{.jsonvalue},          integer                                                        |
|     [\"EKontoEU\"]{.jsonkey}: [ \... ]{.jsonvalue},              integer                                                        |
|     [\"EKontoAusland\"]{.jsonkey}: [ \... ]{.jsonvalue},         integer                                                        |
|     [\"EKontoSteuerfrei\"]{.jsonkey}: [ \... ]{.jsonvalue},      integer                                                        |
|     [\"EKontoAnzInland\"]{.jsonkey}: [ \... ]{.jsonvalue},       integer                                                        |
|     [\"EKontoAnzEU\"]{.jsonkey}: [ \... ]{.jsonvalue},           integer                                                        |
|     [\"EKontoAnzEUOSS\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer, neu ab Version 18.5.0                                 |
|     [\"EKontoAnzAusland\"]{.jsonkey}: [ \... ]{.jsonvalue},      integer                                                        |
|     [\"EKontoAnzSteuerfrei\"]{.jsonkey}: [ \... ]{.jsonvalue},   integer                                                        |
|     [\"AKontoInland\"]{.jsonkey}: [ \... ]{.jsonvalue},          integer                                                        |
|     [\"AKontoEU\"]{.jsonkey}: [ \... ]{.jsonvalue},              integer                                                        |
|     [\"AKontoAusland\"]{.jsonkey}: [ \... ]{.jsonvalue},         integer                                                        |
|     [\"AKontoSteuerfrei\"]{.jsonkey}: [ \... ]{.jsonvalue},      integer                                                        |
|     [\"GesamtRabattGesperrt\"]{.jsonkey}: [ \... ]{.jsonvalue}   boolean (true\|false)                                          |
|   -------------------------------------------------------------- -------------------------------------------------------------- |
|                                                                                                                                 |
| }                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_WarengruppeAddItem .anchor}

::: jsonproto
[WarengruppeAddItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                               |
|                                                                                                                                 |
|   -------------------------------------------------------------- -------------------------------------------------------------- |
|     [\"WarengruppeArt\"]{.jsonkey}: [ \... ]{.jsonvalue},        [Warengruppeart](#Parameter_Warengruppeart){.navlinkcomment}   |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                         |
|     [\"Obergruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string                                                         |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                         |
|     [\"EKontoInland\"]{.jsonkey}: [ \... ]{.jsonvalue},          integer                                                        |
|     [\"EKontoEU\"]{.jsonkey}: [ \... ]{.jsonvalue},              integer                                                        |
|     [\"EKontoAusland\"]{.jsonkey}: [ \... ]{.jsonvalue},         integer                                                        |
|     [\"EKontoSteuerfrei\"]{.jsonkey}: [ \... ]{.jsonvalue},      integer                                                        |
|     [\"EKontoAnzInland\"]{.jsonkey}: [ \... ]{.jsonvalue},       integer                                                        |
|     [\"EKontoAnzEU\"]{.jsonkey}: [ \... ]{.jsonvalue},           integer                                                        |
|     [\"EKontoAnzEUOSS\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer, neu ab Version 18.5.0                                 |
|     [\"EKontoAnzAusland\"]{.jsonkey}: [ \... ]{.jsonvalue},      integer                                                        |
|     [\"EKontoAnzSteuerfrei\"]{.jsonkey}: [ \... ]{.jsonvalue},   integer                                                        |
|     [\"AKontoInland\"]{.jsonkey}: [ \... ]{.jsonvalue},          integer                                                        |
|     [\"AKontoEU\"]{.jsonkey}: [ \... ]{.jsonvalue},              integer                                                        |
|     [\"AKontoAusland\"]{.jsonkey}: [ \... ]{.jsonvalue},         integer                                                        |
|     [\"AKontoSteuerfrei\"]{.jsonkey}: [ \... ]{.jsonvalue},      integer                                                        |
|     [\"GesamtRabattGesperrt\"]{.jsonkey}: [ \... ]{.jsonvalue}   boolean (true\|false)                                          |
|   -------------------------------------------------------------- -------------------------------------------------------------- |
|                                                                                                                                 |
| }                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ArtikelFilter .anchor}

::: jsonproto
[ArtikelFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                |
|                                                                                                                                  |
|   ----------------------------------------------------------------- ------------------------------------------------------------ |
|     [\"Suchtext\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                       |
|     [\"Warengruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                       |
|     [\"Matchcode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                       |
|     [\"Artikelart\"]{.jsonkey}: [ \... ]{.jsonvalue},               [Artikelart](#Parameter_Artikelart){.navlinkcomment}         |
|     [\"Artikelstatus\"]{.jsonkey}: [ \... ]{.jsonvalue},            [Artikelstatus](#Parameter_Artikelstatus){.navlinkcomment}   |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                       |
|     [\"Hersteller\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                       |
|     [\"GesperrteAusblenden\"]{.jsonkey}: [ \... ]{.jsonvalue},      boolean (true\|false)                                        |
|     [\"nurLagerArtikel\"]{.jsonkey}: [ \... ]{.jsonvalue},          boolean (true\|false)                                        |
|     [\"nurOnlineshopArtikel\"]{.jsonkey}: [ \... ]{.jsonvalue},     boolean (true\|false)                                        |
|     [\"nurVorraetigeArtikel\"]{.jsonkey}: [ \... ]{.jsonvalue},     boolean (true\|false)                                        |
|     [\"nurBestellteArtikel\"]{.jsonkey}: [ \... ]{.jsonvalue},      boolean (true\|false)                                        |
|     [\"nurStueckartikel\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)                                        |
|     [\"nurStuecklisten\"]{.jsonkey}: [ \... ]{.jsonvalue},          boolean (true\|false)                                        |
|     [\"ohneStuecklisten\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)                                        |
|     [\"Stueckliste_Ident\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                       |
|     [\"nurUnterMindestBestand\"]{.jsonkey}: [ \... ]{.jsonvalue},   boolean (true\|false), Neu ab 19.0.0                         |
|     [\"nurUnterZielBestand\"]{.jsonkey}: [ \... ]{.jsonvalue}       boolean (true\|false), Neu ab 19.0.0                         |
|   ----------------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                                  |
| }                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ArtikelListItem .anchor}

::: jsonproto
[ArtikelListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                |
|                                                                                                                                  |
|   ------------------------------------------------------------- ---------------------------------------------------------------- |
|     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string, readonly                                                 |
|     [\"Matchcode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string, readonly                                                 |
|     [\"ArtikelArt\"]{.jsonkey}: [ \... ]{.jsonvalue},           [Artikelart](#Parameter_Artikelart){.navlinkcomment}, readonly   |
|     [\"ArtikelNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},        string, readonly                                                 |
|     [\"Warengruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string, readonly                                                 |
|     [\"Warengruppe_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string, readonly                                                 |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}       string                                                           |
|   ------------------------------------------------------------- ---------------------------------------------------------------- |
|                                                                                                                                  |
| }                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ArtikelItem .anchor}

::: jsonproto
[ArtikelItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                      |
|                                                                                                                                                        |
|   ------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string, readonly                                                                 |
|     [\"VersionKey\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string, readonly                                                                 |
|     [\"Matchcode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string, readonly                                                                 |
|     [\"ArtikelArt\"]{.jsonkey}: [ \... ]{.jsonvalue},                 [Artikelart](#Parameter_Artikelart){.navlinkcomment}, readonly                   |
|     [\"ArtikelNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string, readonly                                                                 |
|     [\"Warengruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string, readonly                                                                 |
|     [\"Warengruppe_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string, readonly                                                                 |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                                           |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                                           |
|     [\"Status\"]{.jsonkey}: [\...]{.jsonvalue},                       [Artikelstatus](#Parameter_Artikelstatus){.navlinkcomment}                       |
|     [\"Hersteller\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"HerstellerNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                                           |
|     [\"HerstellerURL\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                           |
|     [\"Einheit\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                           |
|     [\"Groesse\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                           |
|     [\"Verpackung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"GewichtProStk\"]{.jsonkey}: [ \... ]{.jsonvalue},              float (0.0)                                                                      |
|     [\"Gewicht\"]{.jsonkey}: [ \... ]{.jsonvalue},                    float (0.0)                                                                      |
|     [\"EANCode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                           |
|     [\"Gesperrt\"]{.jsonkey}: [ \... ]{.jsonvalue},                   boolean (true\|false)                                                            |
|     [\"Sperrgrund\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                           |
|     [\"Kostenstelle\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                                           |
|     [\"InPreisliste\"]{.jsonkey}: [ \... ]{.jsonvalue},               boolean (true\|false)                                                            |
|     [\"Lagerartikel\"]{.jsonkey}: [ \... ]{.jsonvalue},               boolean (true\|false)                                                            |
|     [\"Lager\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                                           |
|     [\"LagerReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                           |
|     [\"OnlineshopArtikel\"]{.jsonkey}: [ \... ]{.jsonvalue},          boolean (true\|false)                                                            |
|     [\"Bestand\"]{.jsonkey}: [ \... ]{.jsonvalue},                    float (0.0), readonly                                                            |
|     [\"Bestellt\"]{.jsonkey}: [ \... ]{.jsonvalue},                   float (0.0), readonly                                                            |
|     [\"MindestBestand\"]{.jsonkey}: [ \... ]{.jsonvalue},             float (0.0)                                                                      |
|     [\"ZielBestand\"]{.jsonkey}: [ \... ]{.jsonvalue},                float (0.0)                                                                      |
|     [\"BestandZuAb\"]{.jsonkey}: [ \... ]{.jsonvalue},                float (0.0)                                                                      |
|     [\"BestandZuAbGrund\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                           |
|     [\"BestelltZuAb\"]{.jsonkey}: [ \... ]{.jsonvalue},               float (0.0)                                                                      |
|     [\"BestelltZuAbGrund\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                           |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                           |
|     [\"ArtikelBildAnzahl\"]{.jsonkey}: [ \... ]{.jsonvalue},          integer, readonly                                                                |
|     [\"AttachmentIDList\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},       Array vom Typ string, readonly                                                   |
|     [\"StueckListTyp\"]{.jsonkey}: [\...]{.jsonvalue},                [StueckListeTyp](#Parameter_StueckListeTyp){.navlinkcomment}, readonly           |
|     [\"PreisProStkEK\"]{.jsonkey}: [ \... ]{.jsonvalue},              float (0.0), readonly                                                            |
|     [\"PreisProStkVK\"]{.jsonkey}: [ \... ]{.jsonvalue},              float (0.0), readonly                                                            |
|     [\"EKBerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},              [Artikelkalkbasis](#Parameter_Artikelkalkbasis){.navlinkcomment}, readonly       |
|     [\"EKAufwandArt\"]{.jsonkey}: [\...]{.jsonvalue},                 [Artikelkalkaufwand](#Parameter_Artikelkalkaufwand){.navlinkcomment}, readonly   |
|     [\"EKPreisNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string, readonly                                                                 |
|     [\"EKPreisSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string, readonly                                                                 |
|     [\"EKPreisBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string, readonly                                                                 |
|     [\"EKAufwBetragNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string, readonly                                                                 |
|     [\"EKAufwBetragSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string, readonly                                                                 |
|     [\"EKAufwBetragBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string, readonly                                                                 |
|     [\"EKAufwProzentNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string, readonly                                                                 |
|     [\"EKAufwProzentBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string, readonly                                                                 |
|     [\"EKGesamtNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string, readonly                                                                 |
|     [\"EKGesamtSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string, readonly                                                                 |
|     [\"EKGesamtBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string, readonly                                                                 |
|     [\"VKBerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},              [Artikelkalkbasis](#Parameter_Artikelkalkbasis){.navlinkcomment}, readonly       |
|     [\"VKMargeArt\"]{.jsonkey}: [\...]{.jsonvalue},                   [Artikelkalkmarge](#Parameter_Artikelkalkmarge){.navlinkcomment}, readonly       |
|     [\"VKMargeBetragNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string, readonly                                                                 |
|     [\"VKMargeBetragSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string, readonly                                                                 |
|     [\"VKMargeBetragBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string, readonly                                                                 |
|     [\"VKMargeProzentNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string, readonly                                                                 |
|     [\"VKMargeProzentBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string, readonly                                                                 |
|     [\"VKGesamtNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string, readonly                                                                 |
|     [\"VKGesamtSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string, readonly                                                                 |
|     [\"VKGesamtBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}          string, readonly                                                                 |
|   ------------------------------------------------------------------- -------------------------------------------------------------------------------- |
|                                                                                                                                                        |
| }                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ArtikelAddltem .anchor}

::: jsonproto
[ArtikelAddltem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+----------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                            |
|                                                                                                                                              |
|   ------------------------------------------------------------------- ---------------------------------------------------------------------- |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                                 |
|     [\"ArtikelArt\"]{.jsonkey}: [ \... ]{.jsonvalue},                 [Artikelart](#Parameter_Artikelart){.navlinkcomment}                   |
|     [\"ArtikelNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                 |
|     [\"Warengruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},            string                                                                 |
|     [\"Matchcode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},              string                                                                 |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                                 |
|     [\"Status\"]{.jsonkey}: [\...]{.jsonvalue},                       [Artikelstatus](#Parameter_Artikelstatus){.navlinkcomment}             |
|     [\"Hersteller\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                 |
|     [\"HerstellerNr\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                                 |
|     [\"HerstellerURL\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                 |
|     [\"Einheit\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                 |
|     [\"Groesse\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                 |
|     [\"Verpackung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                 |
|     [\"GewichtProStk\"]{.jsonkey}: [ \... ]{.jsonvalue},              float (0.0)                                                            |
|     [\"Gewicht\"]{.jsonkey}: [ \... ]{.jsonvalue},                    float (0.0)                                                            |
|     [\"EANCode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                 |
|     [\"Gesperrt\"]{.jsonkey}: [ \... ]{.jsonvalue},                   boolean (true\|false)                                                  |
|     [\"Sperrgrund\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             string                                                                 |
|     [\"Kostenstelle\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                                 |
|     [\"InPreisliste\"]{.jsonkey}: [ \... ]{.jsonvalue},               boolean (true\|false)                                                  |
|     [\"Lagerartikel\"]{.jsonkey}: [ \... ]{.jsonvalue},               boolean (true\|false)                                                  |
|     [\"Lager\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                  string                                                                 |
|     [\"LagerReferenz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                 |
|     [\"OnlineshopArtikel\"]{.jsonkey}: [ \... ]{.jsonvalue},          boolean (true\|false)                                                  |
|     [\"BestandZuAb\"]{.jsonkey}: [ \... ]{.jsonvalue},                float (0.0)                                                            |
|     [\"BestandZuAbGrund\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                 |
|     [\"BestelltZuAb\"]{.jsonkey}: [ \... ]{.jsonvalue},               float (0.0)                                                            |
|     [\"BestelltZuAbGrund\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                 |
|     [\"MindestBestand\"]{.jsonkey}: [ \... ]{.jsonvalue},             float (0.0)                                                            |
|     [\"ZielBestand\"]{.jsonkey}: [ \... ]{.jsonvalue},                float (0.0)                                                            |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},                string                                                                 |
|     [\"PreisProStkEK\"]{.jsonkey}: [ \... ]{.jsonvalue},              float (0.0)                                                            |
|     [\"PreisProStkVK\"]{.jsonkey}: [ \... ]{.jsonvalue},              float (0.0)                                                            |
|     [\"EKBerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},              [Artikelkalkbasis](#Parameter_Artikelkalkbasis){.navlinkcomment}       |
|     [\"EKAufwandArt\"]{.jsonkey}: [\...]{.jsonvalue},                 [Artikelkalkaufwand](#Parameter_Artikelkalkaufwand){.navlinkcomment}   |
|     [\"EKPreisNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                                                                 |
|     [\"EKPreisSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                 |
|     [\"EKPreisBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                 |
|     [\"EKAufwBetragNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                 |
|     [\"EKAufwBetragSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                                 |
|     [\"EKAufwBetragBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                                 |
|     [\"EKAufwProzentNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                                 |
|     [\"EKAufwProzentBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                                 |
|     [\"EKGesamtNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                 |
|     [\"EKGesamtSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                                 |
|     [\"EKGesamtBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                                 |
|     [\"VKBerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},              [Artikelkalkbasis](#Parameter_Artikelkalkbasis){.navlinkcomment}       |
|     [\"VKMargeArt\"]{.jsonkey}: [\...]{.jsonvalue},                   [Artikelkalkmarge](#Parameter_Artikelkalkmarge){.navlinkcomment}       |
|     [\"VKMargeBetragNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                                 |
|     [\"VKMargeBetragSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                                 |
|     [\"VKMargeBetragBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                                 |
|     [\"VKMargeProzentNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                                                                 |
|     [\"VKMargeProzentBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                 |
|     [\"VKGesamtNetto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},          string                                                                 |
|     [\"VKGesamtSteuer\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                                 |
|     [\"VKGesamtBrutto\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}          string                                                                 |
|   ------------------------------------------------------------------- ---------------------------------------------------------------------- |
|                                                                                                                                              |
| }                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ArtikelAddPosten .anchor}

::: jsonproto
[ArtikelAddPosten]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+
| {                                                                         |
|                                                                           |
|   --------------------------------------------------------- ------------- |
|     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string        |
|     [\"Artikelmenge\"]{.jsonkey}: [ \... ]{.jsonvalue}      float (0.0)   |
|   --------------------------------------------------------- ------------- |
|                                                                           |
| }                                                                         |
+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_ArtikelBildItem .anchor}

::: jsonproto
[ArtikelBildItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                        |
|                                                                                                                          |
|   --------------------------------------------------------- ------------------------------------------------------------ |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                       |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                       |
|     [\"Bildposition\"]{.jsonkey}: [ \... ]{.jsonvalue},     integer, 1 = Position 1,2 = Position 2 usw, 0 ist ungültig   |
|     [\"Bildbreite\"]{.jsonkey}: [ \... ]{.jsonvalue},       integer                                                      |
|     [\"Bildhoehe\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                      |
|     [\"Bildformat\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                       |
|     [\"DatenBASE64\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string, Raw-Daten in BASE64-Kodierung                        |
|   --------------------------------------------------------- ------------------------------------------------------------ |
|                                                                                                                          |
| }                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ArtikelBildAddlItem .anchor}

::: jsonproto
[ArtikelBildAddlItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                       |
|                                                                                                                         |
|   --------------------------------------------------------- ----------------------------------------------------------- |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string                                                      |
|     [\"Bildposition\"]{.jsonkey}: [ \... ]{.jsonvalue},     integer, 0 = Append an Liste , 1 \... n = Insert in Liste   |
|     [\"Notizen\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                      |
|     [\"DatenBASE64\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string, Raw-Daten in BASE64-Kodierung                       |
|   --------------------------------------------------------- ----------------------------------------------------------- |
|                                                                                                                         |
| }                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#artikel .anchor}\

### Funktionsliste von Artikel und Leistungen

[]{#artikel_warengruppeTemplate .anchor}

::::: memitem
::: memproto
[warengruppeTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert WarengruppeAddItem als Vorlage

**Aufruf:**
:   { \"warengruppeTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"warengruppeTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"WarengruppeAddItem\": {\...} } ]{.jsonvalue}   [WarengruppeAddItem](#Parameter_WarengruppeAddItem){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#artikel_warengruppeList .anchor}

::::: memitem
::: memproto
[warengruppeList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung Warengruppen

**Aufruf:**
:   { \"warengruppeList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"warengruppeListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                    |
    |   ------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"WarengruppeListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [WarengruppeListItem](#Parameter_WarengruppeListItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                      |
    | }                                                                                                                                                                                    |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#artikel_warengruppeGet .anchor}

::::: memitem
::: memproto
[warengruppeGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details einer Warengruppe

**Aufruf:**
:   { \"warengruppeGet\":
    +-------------------------------------------------------------------------+
    | {                                                                       |
    |   ------------------------------------------------------------ -------- |
    |     [\"Warengruppe_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ------------------------------------------------------------ -------- |
    |                                                                         |
    | }                                                                       |
    +-------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"warengruppeGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                  |
    |   ------------------------------------------------------------------------------- ---------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"WarengruppeItem\": {\...} } ]{.jsonvalue}   [WarengruppeItem](#Parameter_WarengruppeItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------- ---------------------------------------------------------------- |
    |                                                                                                                                                    |
    | }                                                                                                                                                  |
    +----------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#artikel_warengruppeAdd .anchor}

::::: memitem
::: memproto
[warengruppeAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt eine Warengruppe hinzu

**Aufruf:**
:   { \"warengruppeAdd\":
    +---------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                     |
    |   ------------------------------------------------------------ ---------------------------------------------------------------------- |
    |     [\"WarengruppeAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [WarengruppeAddItem](#Parameter_WarengruppeAddItem){.navlinkcomment}   |
    |   ------------------------------------------------------------ ---------------------------------------------------------------------- |
    |                                                                                                                                       |
    | }                                                                                                                                     |
    +---------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"warengruppeAddResponse\":
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

[]{#artikel_warengruppeDelete .anchor}

::::: memitem
::: memproto
[warengruppeDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht eine vorhandene Warengruppe

**Aufruf:**
:   { \"warengruppeDelete\":
    +-------------------------------------------------------------------------+
    | {                                                                       |
    |   ------------------------------------------------------------ -------- |
    |     [\"Warengruppe_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string   |
    |   ------------------------------------------------------------ -------- |
    |                                                                         |
    | }                                                                       |
    +-------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"warengruppeDeleteResponse\":
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

[]{#artikel_artikelTemplate .anchor}

::::: memitem
::: memproto
[artikelTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
liefert ArtikelAddltem als Vorlage

**Aufruf:**
:   { \"artikelTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"artikelTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                               |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ArtikelAddltem\": {\...} } ]{.jsonvalue}   [ArtikelAddltem](#Parameter_ArtikelAddltem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------ -------------------------------------------------------------- |
    |                                                                                                                                                 |
    | }                                                                                                                                               |
    +-------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#artikel_artikelList .anchor}

::::: memitem
::: memproto
[artikelList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Auflistung Artikel

**Aufruf:**
:   { \"artikelList\":
    +-----------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                 |
    |   ------------------------------------------------------- ----------------------------------------------------------------------- |
    |     [\"ArtikelFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [ArtikelFilter](#Parameter_ArtikelFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------- ----------------------------------------------------------------------- |
    |                                                                                                                                   |
    | }                                                                                                                                 |
    +-----------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"artikelListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                        |
    |   --------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ArtikelListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [ArtikelListItem](#Parameter_ArtikelListItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ |
    |                                                                                                                                                                          |
    | }                                                                                                                                                                        |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#artikel_artikelGet .anchor}

::::: memitem
::: memproto
[artikelGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Details eines Artikel/Leistung

**Aufruf:**
:   { \"artikelGet\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"artikelGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                      |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ArtikelItem\": {\...} } ]{.jsonvalue}   [ArtikelItem](#Parameter_ArtikelItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------- -------------------------------------------------------- |
    |                                                                                                                                        |
    | }                                                                                                                                      |
    +----------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#artikel_artikelAdd .anchor}

::::: memitem
::: memproto
[artikelAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt einen Artikel/Leistung hinzu

**Aufruf:**
:   { \"artikelAdd\":
    +---------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                         |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |     [\"ArtikelAddltem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [ArtikelAddltem](#Parameter_ArtikelAddltem){.navlinkcomment}   |
    |   -------------------------------------------------------- -------------------------------------------------------------- |
    |                                                                                                                           |
    | }                                                                                                                         |
    +---------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"artikelAddResponse\":
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

[]{#artikel_artikelDelete .anchor}

::::: memitem
::: memproto
[artikelDelete]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
löscht einen vorhandene Artikel/Leistung

**Aufruf:**
:   { \"artikelDelete\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   -------------------------------------------------------- --------   |
    |     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
    |   -------------------------------------------------------- --------   |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"artikelDeleteResponse\":
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

[]{#artikel_artikelModify .anchor}

:::::: memitem
::: memproto
[artikelModify]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
ändert einen vorhandenen Artikel/Leistung

::: mohelpinfo
\
Ablauf:\
1. Struktur ArtikelItem über artikelGet abrufen.Es wird ein gültiger VersionKey geliefert.\
2. Daten von ArtikelItem bei Bedarf anpassen.\
3. Funktion artikelModify ausführen.\
Es wird ein Status über Erfolg/Fehler der Operation zurückgeliefert.\
Hinweis: Es sind nicht alle Daten von ArtikelItem modifizierbar.\
\
**Wichtig** Es sollten nur die Parameter übergeben werden, welche auch geändert werden sollen. Alle anderen sollten aus ArtikelItem entfernt werden.\
\
Beispielaufruf Änderung Artikelbezeichnung (Artikel_ID,VersionKey beispielhaft)\
{\
 \"artikelModify\":{\
    \"ArtikelItem\":{\
     \"Artikel_ID\":\"481A62479DF4207DB23598B6461308\",\
     \"VersionKey\":\"99276D86013D6FE47EFB22572D96B63624\",\
     \"Bezeichnung\":\"Hammerstiel holz\"\
   }\
  }\
}
:::

**Aufruf:**
:   { \"artikelModify\":
    +------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                |
    |   ----------------------------------------------------- -------------------------------------------------------- |
    |     [\"ArtikelItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [ArtikelItem](#Parameter_ArtikelItem){.navlinkcomment}   |
    |   ----------------------------------------------------- -------------------------------------------------------- |
    |                                                                                                                  |
    | }                                                                                                                |
    +------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"artikelModifyResponse\":
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

[]{#artikel_artikelFilterTemplate .anchor}

::::: memitem
::: memproto
[artikelFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Filter Artikel/Leistungen

**Aufruf:**
:   { \"artikelFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"artikelFilterTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                            |
    |   ----------------------------------------------------------------------------- ------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ArtikelFilter\": {\...} } ]{.jsonvalue}   [ArtikelFilter](#Parameter_ArtikelFilter){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------- ------------------------------------------------------------ |
    |                                                                                                                                              |
    | }                                                                                                                                            |
    +----------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#artikel_artikelAddAttachment .anchor}

::::: memitem
::: memproto
[artikelAddAttachment]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
fügt ein Attachment einem Artikel hinzu

**Aufruf:**
:   { \"artikelAddAttachment\":
    +------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                  |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                               |
    |     [\"AttachmentAddItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [AttachmentAddItem](#Parameter_AttachmentAddItem){.navlinkcomment}   |
    |   ----------------------------------------------------------- -------------------------------------------------------------------- |
    |                                                                                                                                    |
    | }                                                                                                                                  |
    +------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"artikelAddAttachmentResponse\":
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

[]{#artikel_artikelBildGet .anchor}

:::::: memitem
::: memproto
[artikelBildGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
Abrufen eines Artikelbildes

::: mohelpinfo
\
Artikelbilder werden durch ihre Position in der Bildliste des Artikels addressiert.\
Dabei hat das erste Bild die Bildposition=1,das zweite die Bildposition=2 usw.\
Das Bild wird als Base64-codierter Datensatz geliefert, in dem im Bildformat definierten Format.\
Hinweis: Artikelbilder sind in erster Linie für die Druckausgabe in Einkauf/Verkaufsbelegen vorgesehen.\
Für eine universellere Verknüpfung von Artikeln mit weiteren Daten sollten Attachments verwendet werden.
:::

**Aufruf:**
:   { \"artikelBildGet\":
    +-----------------------------------------------------------------------+
    | {                                                                     |
    |   --------------------------------------------------------- --------- |
    |     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string    |
    |     [\"Bildposition\"]{.jsonkey}: [ \... ]{.jsonvalue}      integer   |
    |   --------------------------------------------------------- --------- |
    |                                                                       |
    | }                                                                     |
    +-----------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"artikelBildGetResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                  |
    |   ------------------------------------------------------------------------------- ---------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ArtikelBildItem\": {\...} } ]{.jsonvalue}   [ArtikelBildItem](#Parameter_ArtikelBildItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------- ---------------------------------------------------------------- |
    |                                                                                                                                                    |
    | }                                                                                                                                                  |
    +----------------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#artikel_artikelBildTemplate .anchor}

::::: memitem
::: memproto
[artikelBildTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Abrufen einer Datenstruktur ArtikelBildAddlItem

**Aufruf:**
:   { \"artikelBildTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"artikelBildTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ArtikelBildAddlItem\": {\...} } ]{.jsonvalue}   [ArtikelBildAddlItem](#Parameter_ArtikelBildAddlItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#artikel_artikelBildAdd .anchor}

:::::: memitem
::: memproto
[artikelBildAdd]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
fügt ein Artikelbild hinzu

::: mohelpinfo
\
Ablauf:\
1. Den Zielartikel über den Parameter Artikel_ID festlegen.\
2. Eine Struktur Datenstruktur ArtikelBildAddlItem über artikelBildTemplate abrufen mit folgenden Daten füllen:\
    2.1 Den Namen des Artikebildes in Name festlegen. Dieser muss innerhalb des Artikels eindeutig sein.\
    2.2 Die Einfügeposition über Bildposition festlegen.\
    Dabei wird bei Wert 0 das Bild an die Bildliste des Artikels angehängt, ansonsten das Bild an der Position eingefügt.\
    2.3 Die eigentlichen Bilddaten Base64-codiert in DatenBASE64 setzen. Unterstützt werden die gängien Bildformate.\
    2.4 Eventuelle Notizen können in Notizen gesetzt werden.\
3. Funktion artikelBildAdd ausführen.\
Es wird dem Artikel das Bild zugeordnet. Bei Erfolg wird der Statuscode=0 geliefert.\
Bei einem Fehler wird Statuscode \<\> 0 und weitere Infos zum aufgetretenen Fehler geliefert.\
\
Hinweis: Weitere Infos zu Artikelbilder finden sie in der Hilfe zur Funktion artikelBildGet.\
Sie können sich mit Hilfe des Testclient mit den Funktionen vertraut machen. Dort werden Testdaten einem auszuwählenden Artikel zugeordnet.
:::

**Aufruf:**
:   { \"artikelBildAdd\":
    +------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                        |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                   |
    |     [\"ArtikelBildAddlItem\"]{.jsonkey}: [ \... ]{.jsonvalue}   [ArtikelBildAddlItem](#Parameter_ArtikelBildAddlItem){.navlinkcomment}   |
    |   ------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                          |
    | }                                                                                                                                        |
    +------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"artikelBildAddResponse\":
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

[]{#Content_lager .anchor}  \

