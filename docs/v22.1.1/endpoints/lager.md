## Lager

[]{#lager_Datenstrukturen .anchor}

### Datenstrukturen von Lager

[]{#Parameter_LagerjournalVorgang .anchor}

::: jsonproto
[LagerjournalVorgang]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| { [\"LagerjournalVorgang\"]{.jsonkey tag="LagerjournalVorgang"}: [\...]{.jsonvalue} } |   ----------------------------------- ---------------------------------------------------------------------------- |
|                                                                                       |   Aufzählung, Integer                 0=[Alle]{tag="Alle"}\                                                        |
|                                                                                       |                                       11=[Eingangs-Bestellung]{tag="Eingangs-Bestellung"}\                         |
|                                                                                       |                                       8=[Eingangs-Rechnung]{tag="Eingangs-Rechnung"}\                              |
|                                                                                       |                                       7=[Eingangs-Warenlieferung]{tag="Eingangs-Warenlieferung"}\                  |
|                                                                                       |                                       10=[Eingangs-Lieferantengutschrift]{tag="Eingangs-Lieferantengutschrift"}\   |
|                                                                                       |                                       5=[Ausgangs-Lieferschein]{tag="Ausgangs-Lieferschein"}\                      |
|                                                                                       |                                       6=[Ausgangs-Rechnung]{tag="Ausgangs-Rechnung"}\                              |
|                                                                                       |                                       9=[Ausgangs-Korrekturrechnung]{tag="Ausgangs-Korrekturrechnung"}\            |
|                                                                                       |                                       20=[Korrektur Zugang (Bestand)]{tag="Korrektur Zugang (Bestand)"}\           |
|                                                                                       |                                       18=[Korrektur Abgang (Bestand)]{tag="Korrektur Abgang (Bestand)"}\           |
|                                                                                       |                                       21=[Korrektur Zugang (Bestellt)]{tag="Korrektur Zugang (Bestellt)"}\         |
|                                                                                       |                                       19=[Korrektur Abgang (Bestellt)]{tag="Korrektur Abgang (Bestellt)"}\         |
|                                                                                       |                                       1=[Manueller Zugang (Bestand)]{tag="Manueller Zugang (Bestand)"}\            |
|                                                                                       |                                       2=[Manueller Abgang (Bestand)]{tag="Manueller Abgang (Bestand)"}\            |
|                                                                                       |                                       3=[Manueller Zugang (Bestellt)]{tag="Manueller Zugang (Bestellt)"}\          |
|                                                                                       |                                       4=[Manueller Abgang (Bestellt)]{tag="Manueller Abgang (Bestellt)"}\          |
|                                                                                       |                                       29=[Stückliste Zugang (Bestand)]{tag="Stückliste Zugang (Bestand)"}\         |
|                                                                                       |                                       30=[Stückliste Abgang (Bestand)]{tag="Stückliste Abgang (Bestand)"}          |
|                                                                                       |                                                                                                                    |
|                                                                                       |   ----------------------------------- ---------------------------------------------------------------------------- |
+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_LagerjournalFilter .anchor}

::: jsonproto
[LagerjournalFilter]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+------------------------------------------------------------------------------------------------------------+
| {                                                                                                          |
|                                                                                                            |
|   ----------------------------------------------------------------- -------------------------------------- |
|     [\"DatumVon\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             date (yyyy-mm-dd)                      |
|     [\"DatumBis\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},             date (yyyy-mm-dd)                      |
|     [\"LagerjournalVorgang\"]{.jsonkey}: [ \... ]{.jsonvalue},      integer                                |
|     [\"Vortragswerte\"]{.jsonkey}: [ \... ]{.jsonvalue},            boolean (true\|false)                  |
|     [\"NurLetzeBewegung\"]{.jsonkey}: [ \... ]{.jsonvalue},         boolean (true\|false)                  |
|     [\"nurUnterMindestBestand\"]{.jsonkey}: [ \... ]{.jsonvalue},   boolean (true\|false), Neu ab 19.0.0   |
|     [\"nurUnterZielBestand\"]{.jsonkey}: [ \... ]{.jsonvalue},      boolean (true\|false), Neu ab 19.0.0   |
|     [\"nurMitBestellungen\"]{.jsonkey}: [ \... ]{.jsonvalue}        boolean (true\|false), Neu ab 19.0.0   |
|   ----------------------------------------------------------------- -------------------------------------- |
|                                                                                                            |
| }                                                                                                          |
+------------------------------------------------------------------------------------------------------------+
:::

\
[]{#Parameter_LagerjournalItem .anchor}

::: jsonproto
[LagerjournalItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                         |
|                                                                                                                                           |
|   -------------------------------------------------------------- ------------------------------------------------------------------------ |
|     [\"EingabeDatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      date (yyyy-mm-dd)                                                        |
|     [\"Buchungdatum\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},      date (yyyy-mm-dd)                                                        |
|     [\"LagerjournalVorgang\"]{.jsonkey}: [ \... ]{.jsonvalue},   [LagerjournalVorgang](#Parameter_LagerjournalVorgang){.navlinkcomment}   |
|     [\"VorgangInfo\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},       string                                                                   |
|     [\"Menge\"]{.jsonkey}: [ \... ]{.jsonvalue},                 float (0.0)                                                              |
|     [\"Bestellt\"]{.jsonkey}: [ \... ]{.jsonvalue},              float (0.0)                                                              |
|     [\"Bestand\"]{.jsonkey}: [ \... ]{.jsonvalue}                float (0.0)                                                              |
|   -------------------------------------------------------------- ------------------------------------------------------------------------ |
|                                                                                                                                           |
| }                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------+
:::

\
[]{#lager .anchor}\

### Funktionsliste von Lager

[]{#lager_lagerartikelList .anchor}

::::: memitem
::: memproto
[lagerartikelList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Listet alle Lagerartikel

**Aufruf:**
:   { \"lagerartikelList\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"lagerartikelListResponse\":
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

[]{#lager_lagerjournalFilterTemplate .anchor}

::::: memitem
::: memproto
[lagerjournalFilterTemplate]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Vorlage für Lagerjournal-Filter

**Aufruf:**
:   { \"lagerjournalFilterTemplate\":\"\"}

<!-- -->

**Rückgabe:**
:   { \"lagerjournalFilterTemplateResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                           |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"LagerjournalFilter\": {\...} } ]{.jsonvalue}   [LagerjournalFilter](#Parameter_LagerjournalFilter){.navlinkcomment}   |
    |   ---------------------------------------------------------------------------------- ---------------------------------------------------------------------- |
    |                                                                                                                                                             |
    | }                                                                                                                                                           |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#lager_lagerjournalList .anchor}

::::: memitem
::: memproto
[lagerjournalList]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Lagerjournal(mit filter)

**Aufruf:**
:   { \"lagerjournalList\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |     [\"LagerjournalFilter\"]{.jsonkey}: [ \... ]{.jsonvalue}   [LagerjournalFilter](#Parameter_LagerjournalFilter){.navlinkcomment} (optional)   |
    |   ------------------------------------------------------------ --------------------------------------------------------------------------------- |
    |                                                                                                                                                  |
    | }                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"lagerjournalListResponse\":
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                                                                |
    |   ----------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------- |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"LagerjournalArtikelItem\": \[ {}, \... \] } ]{.jsonvalue}   Array vom Typ [LagerjournalArtikelItem](#Parameter_LagerjournalArtikelItem){.navlinkcomment}   |
    |   ----------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------- |
    |                                                                                                                                                                                                  |
    | }                                                                                                                                                                                                |
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#lager_lagerjournalGet .anchor}

::::: memitem
::: memproto
[lagerjournalGet]{.memname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: memdoc
Liefert Lagerjournal für Artikel (mit ID)

**Aufruf:**
:   { \"lagerjournalGet\":
    +-------------------------------------------------------------------------------------------------+
    | {                                                                                               |
    |   ---------------------------------------------------------- ---------------------------------- |
    |     [\"Artikel_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue},    string                             |
    |     [\"NurLetzeBewegung\"]{.jsonkey}: [ \... ]{.jsonvalue}   boolean (true\|false) (optional)   |
    |   ---------------------------------------------------------- ---------------------------------- |
    |                                                                                                 |
    | }                                                                                               |
    +-------------------------------------------------------------------------------------------------+

    }

<!-- -->

**Rückgabe:**
:   { \"lagerjournalGetResponse\":
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+
    | {                                                                                                                                                     |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |     [\"ReturnData\"]{.jsonkey}: [ { \"LagerjournalItem\": {\...} } ]{.jsonvalue}   [LagerjournalItem](#Parameter_LagerjournalItem){.navlinkcomment}   |
    |   -------------------------------------------------------------------------------- ------------------------------------------------------------------ |
    |                                                                                                                                                       |
    | }                                                                                                                                                     |
    +-------------------------------------------------------------------------------------------------------------------------------------------------------+

    }
:::
:::::

[]{#Content_verkauf .anchor}  \

