## A StillNincsenCsapatnév nevű csapat munkája

# A webapplikáció használata
A főoldalt az ip címen érjük el.

### Versenyzőként való használat
Bejelentkezni a navigációs sávban lévő Bejelentkezés linkre való kattintás után tudunk. Ha nincs fiókunk, akkor a Regisztrációra kell kattintani.

Regisztrációnál egy beépített Django felhasználót hotunk létre, amely egy alap Role-t kap, ami a versenyzői szerepkör.

Ez után be kell jelentkeznünk. Bejelentkezés után a képernyő, amit kapunk a jelenlegi verseny határidejétől függ. Ha le van zárva a jelentkezés, vagy lejárt a jelentkezési határidő, akkor egy üzenetet kapunk, hogy majd a következő jelentkezési időszakban tudunk csapatot regisztrálni.

Ha lehet csapatot regisztrálni, akkor megkapjuk rá a lehetőséget egy gomb formájában. Ez átirányít minket egy oldalra, ahol regisztrálni tudunk egy csapatot, ami ez után látható lesz a felhasználó számára, miután bejelentkezett. Az ehhez tartozó adatokat a verseny leírásának megfelelően tudja módosítani később.

Ha egy szervező hiánypótlásra küldött ki kérést, akkor a jobb felső sarokból lehet azt elérni.

Kijelentkezni jobb felül a felhasználónév melletti kijelentkezés gombbal lehet.

### Szervezőként való használat
Szervezőt regisztrálni nem lehet biztonsági okokból. A DJangoAdmin felületen tud a superuser létrehozni egy user-t, és ahhoz organiser Role-t adni.

Bejelentkezés után egy irányító pult fogad minket.\
Lehetőségünk van módosítani a jeletnkezési határidőt, vagy akár lezárni a jelentkezéseket.

Emellett (Ajax kérésekkel megoldva) tudunk kategóriákat és programnyelveket kezelni. A beviteli mezőbe írva a kívánt szöveget, majd a hozzáadás gombot megnyomva. Ha törölni akarunk, akkro pedig értelemszerűen a törlés gombot kell használnunk.

Szervezőként lehetőségünk van a regisztrált iskolák megjelenítésére, és akár új iskolák regisztrálására. Ezt a navigációs sávban érjük el az Iskolák megtekintése fül alatt.

A jelentkezéseket a navigációs sávból érjük el. Itt lehetőségünk van letölteni egy .csv fájlt, ami tartalmazza az összes csapat adatát. Ha egy csapatot szeretnénk kezelni, a mellette lévő Több gombot kell megnyomnunk. Itt látjuk a részletes adatokat, illetve megvan a lehetőség a jóváhagyásra, illetve a pdf letöltésére, amit az igazgató töltött fel, mikor jóváhagyta az iskolájából jelentkező csapat jelentkezését. Ha hiányosnak akarjuk jelenteni a jelentkezést, akkor egy beviteli mezőbe tudjuk írni az üzenetünket, majd elküldhetjük.

### Iskolai kapcsolattartóként való használat
Bejelentkezés után az iskola adataival fogad minket a weblap. Igény esetén ezek módosíthatóak. Alább pedig az iskola neve alatt jelentkezett csapatokat láthatjuk. Mellettük egy gomb, Jóváhagyás címmel. Erre kattintva feltölthetünk egy pdf-et, ezzel jóváhagyva a csapat jelentkezését.
