## Vorgaben

[]{#vorgaben_Datenstrukturen .anchor}

### Datenstrukturen von Vorgaben

[]{#Parameter_Zahlungsart .anchor}

::: jsonproto
[Zahlungsart]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------+
| { [\"Zahlungsart\"]{.jsonkey tag="Zahlungsart"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------- |
|                                                                       |   Aufzählung, Integer                 0=[Keine]{tag="Keine"}\                 |
|                                                                       |                                       1=[Bar]{tag="Bar"}\                     |
|                                                                       |                                       2=[Lastschrift]{tag="Lastschrift"}\     |
|                                                                       |                                       3=[Kreditkarte]{tag="Kreditkarte"}\     |
|                                                                       |                                       4=[Überweisung]{tag="Überweisung"}\     |
|                                                                       |                                       5=[Scheck]{tag="Scheck"}\               |
|                                                                       |                                       6=[Verrechnung]{tag="Verrechnung"}\     |
|                                                                       |                                       7=[Girokarte]{tag="Girokarte"}\         |
|                                                                       |                                       8=[Finanzierung]{tag="Finanzierung"}\   |
|                                                                       |                                       9=[Debit-Karte]{tag="Debit-Karte"}      |
|                                                                       |                                                                               |
|                                                                       |   ----------------------------------- --------------------------------------- |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------+
:::

\
[]{#Parameter_Zahlungstatus .anchor}

::: jsonproto
[Zahlungstatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"Zahlungstatus\"]{.jsonkey tag="Zahlungstatus"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                           |   Aufzählung, Integer                 0=[Ohne]{tag="Ohne"}\               |
|                                                                           |                                       1=[Offen]{tag="Offen"}\             |
|                                                                           |                                       2=[Teilweise]{tag="Teilweise"}\     |
|                                                                           |                                       3=[Bezahlt]{tag="Bezahlt"}          |
|                                                                           |                                                                           |
|                                                                           |   ----------------------------------- ----------------------------------- |
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_Steuergebiet .anchor}

::: jsonproto
[Steuergebiet]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| { [\"Steuergebiet\"]{.jsonkey tag="Steuergebiet"}: [\...]{.jsonvalue} } |   ----------------------------------- ------------------------------------------- |
|                                                                         |   Aufzählung, Integer                 1=[Inland]{tag="Inland"}\                   |
|                                                                         |                                       2=[EU-Ausland]{tag="EU-Ausland"}\           |
|                                                                         |                                       5=[EU-Ausland-OSS]{tag="EU-Ausland-OSS"}\   |
|                                                                         |                                       3=[Ausland]{tag="Ausland"}\                 |
|                                                                         |                                       4=[Steuerfrei]{tag="Steuerfrei"}            |
|                                                                         |                                                                                   |
|                                                                         |   ----------------------------------- ------------------------------------------- |
+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
:::

\
[]{#Parameter_KostenstelleListItem .anchor}

::: jsonproto
[KostenstelleListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------+
| {                                                                      |
|                                                                        |
|   ----------------------------------------------------------- -------- |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string   |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string   |
|     [\"Bemerkung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}       string   |
|   ----------------------------------------------------------- -------- |
|                                                                        |
| }                                                                      |
+------------------------------------------------------------------------+
:::

\
[]{#Parameter_NummernkreisListItem .anchor}

::: jsonproto
[NummernkreisListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                 |
|                                                                                                                                   |
|   -------------------------------------------------------- ---------------------------------------------------------------------- |
|     [\"NKIdent\"]{.jsonkey}: [\...]{.jsonvalue},           [NummernkreisIdents](#Parameter_NummernkreisIdents){.navlinkcomment}   |
|     [\"Gruppe\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                                 |
|     [\"Bereich\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                                                                 |
|     [\"Aktuell\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string, Beispielwert, ist zeitpunktabhängig, deprecated                |
|     [\"Nachfolger\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string, Beispielwert, ist zeitpunktabhängig                            |
|   -------------------------------------------------------- ---------------------------------------------------------------------- |
|                                                                                                                                   |
| }                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_SteuersatzListItem .anchor}

::: jsonproto
[SteuersatzListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------+
| {                                                                                     |
|                                                                                       |
|   ----------------------------------------------------------- ----------------------- |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},           string                  |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                  |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},     string                  |
|     [\"Gesperrt\"]{.jsonkey}: [ \... ]{.jsonvalue},           boolean (true\|false)   |
|     [\"OSS_Steuersatz\"]{.jsonkey}: [ \... ]{.jsonvalue}      boolean (true\|false)   |
|   ----------------------------------------------------------- ----------------------- |
|                                                                                       |
| }                                                                                     |
+---------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_WaehrungListItem .anchor}

::: jsonproto
[WaehrungListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------+
| {                                                                      |
|                                                                        |
|   ------------------------------------------------------ ------------- |
|     [\"Name\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string        |
|     [\"Isocode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string        |
|     [\"Kurs\"]{.jsonkey}: [ \... ]{.jsonvalue}           float (0.0)   |
|   ------------------------------------------------------ ------------- |
|                                                                        |
| }                                                                      |
+------------------------------------------------------------------------+
:::

\
[]{#Parameter_VerkaufpreislisteListItem .anchor}

::: jsonproto
[VerkaufpreislisteListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                   |
|                                                                                                                                     |
|   -------------------------------------------------------------- ------------------------------------------------------------------ |
|     [\"VKPreisliste_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                             |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                             |
|     [\"Beschreibung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                             |
|     [\"Standard\"]{.jsonkey}: [ \... ]{.jsonvalue},              boolean (true\|false)                                              |
|     [\"BerechnungArt\"]{.jsonkey}: [\...]{.jsonvalue},           [Artikelkalkbasis](#Parameter_Artikelkalkbasis){.navlinkcomment}   |
|     [\"MargeArt\"]{.jsonkey}: [\...]{.jsonvalue}                 [Artikelkalkmarge](#Parameter_Artikelkalkmarge){.navlinkcomment}   |
|   -------------------------------------------------------------- ------------------------------------------------------------------ |
|                                                                                                                                     |
| }                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ZahlungsBedingungEinkaufListItem .anchor}

::: jsonproto
[ZahlungsBedingungEinkaufListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                     |
|                                                                                                                       |
|   ---------------------------------------------------------- -------------------------------------------------------- |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                   |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue},       [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}   |
|     [\"TageNetto\"]{.jsonkey}: [ \... ]{.jsonvalue},         integer                                                  |
|     [\"TageSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                  |
|     [\"ProzentSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},     float (0.0)                                              |
|     [\"Standard\"]{.jsonkey}: [ \... ]{.jsonvalue}           boolean (true\|false), neu ab Version 22.1               |
|   ---------------------------------------------------------- -------------------------------------------------------- |
|                                                                                                                       |
| }                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_ZahlungsBedingungVerkaufListItem .anchor}

::: jsonproto
[ZahlungsBedingungVerkaufListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                     |
|                                                                                                                       |
|   ---------------------------------------------------------- -------------------------------------------------------- |
|     [\"Bezeichnung\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                   |
|     [\"Zahlungsart\"]{.jsonkey}: [ \... ]{.jsonvalue},       [Zahlungsart](#Parameter_Zahlungsart){.navlinkcomment}   |
|     [\"TageNetto\"]{.jsonkey}: [ \... ]{.jsonvalue},         integer                                                  |
|     [\"TageSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},        integer                                                  |
|     [\"ProzentSkonto\"]{.jsonkey}: [ \... ]{.jsonvalue},     float (0.0)                                              |
|     [\"NichtMahnen\"]{.jsonkey}: [ \... ]{.jsonvalue},       boolean (true\|false)                                    |
|     [\"Standard\"]{.jsonkey}: [ \... ]{.jsonvalue}           boolean (true\|false), neu ab Version 22.1               |
|   ---------------------------------------------------------- -------------------------------------------------------- |
|                                                                                                                       |
| }                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_NummernkreisIdents .anchor}

::: jsonproto
[NummernkreisIdents]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| { [\"NummernkreisIdents\"]{.jsonkey tag="NummernkreisIdents"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------------------------------------- |
|                                                                                     |   Aufzählung, Integer                 8=[Stammdaten Adresse]{tag="Stammdaten Adresse"}\                          |
|                                                                                     |                                       6=[Stammdaten Artikel]{tag="Stammdaten Artikel"}\                          |
|                                                                                     |                                       7=[Stammdaten Leistung]{tag="Stammdaten Leistung"}\                        |
|                                                                                     |                                       25=[Verkauf Kostenvoranschlag]{tag="Verkauf Kostenvoranschlag"}\           |
|                                                                                     |                                       1=[Verkauf Angebot]{tag="Verkauf Angebot"}\                                |
|                                                                                     |                                       2=[Verkauf Auftragsbestätigung]{tag="Verkauf Auftragsbestätigung"}\        |
|                                                                                     |                                       3=[Verkauf Lieferschein]{tag="Verkauf Lieferschein"}\                      |
|                                                                                     |                                       4=[Verkauf Rechnung]{tag="Verkauf Rechnung"}\                              |
|                                                                                     |                                       5=[Verkauf Korrekturrechnung]{tag="Verkauf Korrekturrechnung"}\            |
|                                                                                     |                                       9=[Verkauf Abschlagsrechnung]{tag="Verkauf Abschlagsrechnung"}\            |
|                                                                                     |                                       17=[Verkauf Proformarechnung]{tag="Verkauf Proformarechnung"}\             |
|                                                                                     |                                       10=[Einkauf Bestellanfrage]{tag="Einkauf Bestellanfrage"}\                 |
|                                                                                     |                                       11=[Einkauf Bestellung]{tag="Einkauf Bestellung"}\                         |
|                                                                                     |                                       12=[Einkauf Wareneingang]{tag="Einkauf Wareneingang"}\                     |
|                                                                                     |                                       13=[Einkauf Eingangsrechnung]{tag="Einkauf Eingangsrechnung"}\             |
|                                                                                     |                                       14=[Einkauf Lieferantengutschrift]{tag="Einkauf Lieferantengutschrift"}\   |
|                                                                                     |                                       15=[Einkauf Rücksendung]{tag="Einkauf Rücksendung"}\                       |
|                                                                                     |                                       16=[Einkauf Storno]{tag="Einkauf Storno"}\                                 |
|                                                                                     |                                       20=[ ]{tag=" "}\                                                           |
|                                                                                     |                                       21=[ ]{tag=" "}\                                                           |
|                                                                                     |                                       19=[Buchhaltung Buchung]{tag="Buchhaltung Buchung"}                        |
|                                                                                     |                                                                                                                  |
|                                                                                     |   ----------------------------------- -------------------------------------------------------------------------- |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_DruckFormularGruppen .anchor}

::: jsonproto
[DruckFormularGruppen]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| { [\"DruckFormularGruppen\"]{.jsonkey tag="DruckFormularGruppen"}: [\...]{.jsonvalue} } |   ----------------------------------- ----------------------------------- |
|                                                                                         |   Aufzählung, Integer                 1008=[Verkauf]{tag="Verkauf"}\      |
|                                                                                         |                                       1014=[Einkauf]{tag="Einkauf"}       |
|                                                                                         |                                                                           |
|                                                                                         |   ----------------------------------- ----------------------------------- |
+-----------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_DruckFormularFilter .anchor}

::: jsonproto
[DruckFormularFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------+
| {                                                                         |
|                                                                           |
|   ------------------------------------------------------------- --------- |
|     [\"Suchtext\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},         string    |
|     [\"DruckformularGruppe\"]{.jsonkey}: [ \... ]{.jsonvalue}   integer   |
|   ------------------------------------------------------------- --------- |
|                                                                           |
| }                                                                         |
+---------------------------------------------------------------------------+
:::

\
[]{#Parameter_DruckFormularListItem .anchor}

::: jsonproto
[DruckFormularListItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                             |
|                                                                                                                                               |
|   ---------------------------------------------------------------- -------------------------------------------------------------------------- |
|     [\"DruckformularName\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                                     |
|     [\"DruckformularGruppe\"]{.jsonkey}: [\...]{.jsonvalue}        [DruckFormularGruppen](#Parameter_DruckFormularGruppen){.navlinkcomment}   |
|   ---------------------------------------------------------------- -------------------------------------------------------------------------- |
|                                                                                                                                               |
| }                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_EtikettTags .anchor}

::: jsonproto
[EtikettTags]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| { [\"EtikettTags\"]{.jsonkey tag="EtikettTags"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------------- |
|                                                                       |   Aufzählung, Integer                 0=[Kein EtikettTag]{tag="Kein EtikettTag"}\   |
|                                                                       |                                       1=[EtikettTag 1]{tag="EtikettTag 1"}\         |
|                                                                       |                                       2=[EtikettTag 2]{tag="EtikettTag 2"}\         |
|                                                                       |                                       4=[EtikettTag 3]{tag="EtikettTag 3"}\         |
|                                                                       |                                       8=[EtikettTag 4]{tag="EtikettTag 4"}\         |
|                                                                       |                                       16=[EtikettTag 5]{tag="EtikettTag 5"}\        |
|                                                                       |                                       32=[EtikettTag 6]{tag="EtikettTag 6"}\        |
|                                                                       |                                       64=[EtikettTag 7]{tag="EtikettTag 7"}         |
|                                                                       |                                                                                     |
|                                                                       |   ----------------------------------- --------------------------------------------- |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_FestschreibStatus .anchor}

::: jsonproto
[FestschreibStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| { [\"FestschreibStatus\"]{.jsonkey tag="FestschreibStatus"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------- |
|                                                                                   |   Aufzählung, Integer                 4=[Alle]{tag="Alle"}\                        |
|                                                                                   |                                       1=[Erfasst]{tag="Erfasst"}\                  |
|                                                                                   |                                       2=[Festgeschrieben]{tag="Festgeschrieben"}   |
|                                                                                   |                                                                                    |
|                                                                                   |   ----------------------------------- -------------------------------------------- |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_OSSDatenItem .anchor}

::: jsonproto
[OSSDatenItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+--------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                              |
|                                                                                                                                |
|   --------------------------------------------------------- ------------------------------------------------------------------ |
|     [\"Isocode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      string                                                             |
|     [\"Steuersatz\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},   string                                                             |
|     [\"Typ\"]{.jsonkey}: [\...]{.jsonvalue}                 [SteuersatzOSSTyp](#Parameter_SteuersatzOSSTyp){.navlinkcomment}   |
|   --------------------------------------------------------- ------------------------------------------------------------------ |
|                                                                                                                                |
| }                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_SteuersatzOSSTyp .anchor}

::: jsonproto
[SteuersatzOSSTyp]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| { [\"SteuersatzOSSTyp\"]{.jsonkey tag="SteuersatzOSSTyp"}: [\...]{.jsonvalue} } |   ----------------------------------- -------------------------------------------- |
|                                                                                 |   Aufzählung, Integer                 1=[Steuer normal]{tag="Steuer normal"}\      |
|                                                                                 |                                       2=[Steuer ermäßigt]{tag="Steuer ermäßigt"}   |
|                                                                                 |                                                                                    |
|                                                                                 |   ----------------------------------- -------------------------------------------- |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
:::

\
[]{#vorgaben .anchor}\

### Funktionsliste von Vorgaben

[]{#vorgaben_kostenstellenList .anchor}

::::: memitem
::: memproto
[kostenstellenList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert definierte Kostenstellen

**Aufruf:**
:   { \"kostenstellenList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"kostenstellenListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"KostenstelleListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [KostenstelleListItem](#Parameter_KostenstelleListItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                         |
    | }                                                                                                                                                                                       |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_nummernkreisList .anchor}

::::: memitem
::: memproto
[nummernkreisList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert definierte Nummerkreise

**Aufruf:**
:   { \"nummernkreisList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"nummernkreisListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                       |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"NummernkreisListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [NummernkreisListItem](#Parameter_NummernkreisListItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                         |
    | }                                                                                                                                                                                       |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_steuersatzList .anchor}

::::: memitem
::: memproto
[steuersatzList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert definierte Steuersätze

**Aufruf:**
:   { \"steuersatzList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"steuersatzListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                 |
    |   ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"SteuersatzListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [SteuersatzListItem](#Parameter_SteuersatzListItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------ |
    |                                                                                                                                                                                   |
    | }                                                                                                                                                                                 |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_waehrungList .anchor}

::::: memitem
::: memproto
[waehrungList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert definierte Währungen

**Aufruf:**
:   { \"waehrungList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"waehrungListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"WaehrungListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [WaehrungListItem](#Parameter_WaehrungListItem){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------------- -------------------------------------------------------------------------------- |
    |                                                                                                                                                                             |
    | }                                                                                                                                                                           |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_preislisteVerkaufList .anchor}

::::: memitem
::: memproto
[preislisteVerkaufList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert definierte VK-Preisliste

**Aufruf:**
:   { \"preislisteVerkaufList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"preislisteVerkaufListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                      |
    |   ------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"VerkaufpreislisteListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [VerkaufpreislisteListItem](#Parameter_VerkaufpreislisteListItem){.navlinkcomment}   |
    |   ------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                        |
    | }                                                                                                                                                                                                      |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_zahlungsbedingungEinkaufList .anchor}

::::: memitem
::: memproto
[zahlungsbedingungEinkaufList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert definierte Zahlungsbedingungen Einkauf

**Aufruf:**
:   { \"zahlungsbedingungEinkaufList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"zahlungsbedingungEinkaufListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                                           |
    |   -------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ZahlungsBedingungEinkaufListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [ZahlungsBedingungEinkaufListItem](#Parameter_ZahlungsBedingungEinkaufListItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                                             |
    | }                                                                                                                                                                                                                           |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_zahlungsbedingungVerkaufList .anchor}

::::: memitem
::: memproto
[zahlungsbedingungVerkaufList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert definierte Zahlungsbedingungen Verkauf

**Aufruf:**
:   { \"zahlungsbedingungVerkaufList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"zahlungsbedingungVerkaufListResponse\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                                           |
    |   -------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"ZahlungsBedingungVerkaufListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [ZahlungsBedingungVerkaufListItem](#Parameter_ZahlungsBedingungVerkaufListItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                                             |
    | }                                                                                                                                                                                                                           |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_druckformularFilterTemplate .anchor}

::::: memitem
::: memproto
[druckformularFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Filter für Druckformulare

**Aufruf:**
:   { \"druckformularFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"druckformularFilterTemplateResponse\":
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                              |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DruckFormularFilter\": {\...} } ]{.jsonvalue}   [DruckFormularFilter](#Parameter_DruckFormularFilter){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------- ------------------------------------------------------------------------ |
    |                                                                                                                                                                |
    | }                                                                                                                                                              |
    +----------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_druckformularList .anchor}

::::: memitem
::: memproto
[druckformularList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert definierte Druckformulare

**Aufruf:**
:   { \"druckformularList\":
    +-----------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                   |
    |   ------------------------------------------------------------- ----------------------------------------------------------------------------------- |
    |     [\"DruckFormularFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [DruckFormularFilter](#Parameter_DruckFormularFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------------- ----------------------------------------------------------------------------------- |
    |                                                                                                                                                     |
    | }                                                                                                                                                   |
    +-----------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"druckformularListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                          |
    |   --------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"DruckFormularListItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [DruckFormularListItem](#Parameter_DruckFormularListItem){.navlinkcomment}   |
    |   --------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------ |
    |                                                                                                                                                                                            |
    | }                                                                                                                                                                                          |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#vorgaben_steuersatzOSSList .anchor}

:::::: memitem
::: memproto
[steuersatzOSSList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

:::: memdoc
Liefert OSS-Steuersatzdaten

::: mohelpinfo
\
Es werden die im Programm hinterlegten Daten der Steuersätze für die Anwendung des OSS-Verfahrens geliefert\
Adressiert werden die Daten über den Länderkennzeichen im ISO-Code.\
Verwendung finden die Daten bei Verkaufsbelegen, Debitorenrechnungen, Buchungen.\
\
Voraussetzung ist, das dem verwendete Erlöskonto ein OSS-Steuersatz zugewiesen wurde. Anderenfalls werden die Daten ignoriert.
:::

**Aufruf:**
:   { \"steuersatzOSSList\":
    +-----------------------------------------------------------------------------+
    | {                                                                           |
    |   ----------------------------------------------------- ------------------- |
    |     [\"Isocode\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string (optional)   |
    |   ----------------------------------------------------- ------------------- |
    |                                                                             |
    | }                                                                           |
    +-----------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"steuersatzOSSListResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                         |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"OSSDatenItem\": {\...} } ]{.jsonvalue}   [OSSDatenItem](#Parameter_OSSDatenItem){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------- ---------------------------------------------------------- |
    |                                                                                                                                           |
    | }                                                                                                                                         |
    +-------------------------------------------------------------------------------------------------------------------------------------------+

    }
::::
::::::

[]{#Content_adressen .anchor}  \

