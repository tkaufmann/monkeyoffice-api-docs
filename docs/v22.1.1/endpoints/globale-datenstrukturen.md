## Globale Datenstrukturen

::: jsonproto
[]{#Parameter_ReturnStatus .anchor} [ReturnStatus]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| {                                                                                                                                                       |
|                                                                                                                                                         |
|   ------------------------------------------------------------- --------------------------------------------------------------------------------------- |
|     [\"Statuscode\"]{.jsonkey}: [ \... ]{.jsonvalue},           [Statuscode](#Parameter_Statuscode){.navlinkcomment}                                    |
|     [\"StatustextItem\"]{.jsonkey}: [ \[\...\] ]{.jsonvalue},   Array vom Typ [StatustextItem](#Parameter_StatustextItem){.navlinkcomment} (optional)   |
|     [\"Insert_ID\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}         string (optional)                                                                       |
|   ------------------------------------------------------------- --------------------------------------------------------------------------------------- |
|                                                                                                                                                         |
| }                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+
:::

\

::: jsonproto
[]{#Parameter_Statuscode .anchor} [Statuscode]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| { [\"Statuscode\"]{.jsonkey tag="Statuscode"}: [\...]{.jsonvalue} } |   ----------------------------------- --------------------------------------------------------- |
|                                                                     |   Aufzählung, Integer                 0=[alles OK]{tag="alles OK"}\                             |
|                                                                     |                                       1=[allgemeiner Fehler]{tag="allgemeiner Fehler"}\         |
|                                                                     |                                       2=[Fehler Zugriffsrechte]{tag="Fehler Zugriffsrechte"}\   |
|                                                                     |                                       3=[Funktion unbekannt]{tag="Funktion unbekannt"}\         |
|                                                                     |                                       4=[Parameterfehler]{tag="Parameterfehler"}                |
|                                                                     |                                                                                                 |
|                                                                     |   ----------------------------------- --------------------------------------------------------- |
+---------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
:::

\

::: jsonproto
[]{#Parameter_StatustextItem .anchor} [StatustextItem]{.jsonname}    [Top](#navigation){.navlink}  [Back](javascript:history.go(-1)){.navlink}
:::

::: jsondoc
+-----------------------------------------------------------------------+
| {                                                                     |
|                                                                       |
|   -------------------------------------------------------- --------   |
|     [\"Statustext\"]{.jsonkey}: [ \"\...\" ]{.jsonvalue}   string     |
|   -------------------------------------------------------- --------   |
|                                                                       |
| }                                                                     |
+-----------------------------------------------------------------------+
:::

\
[]{#Content_firmen .anchor}  \

