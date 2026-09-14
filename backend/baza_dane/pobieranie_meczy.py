import os
import httpx


from dotenv import load_dotenv

load_dotenv()

ADRES_API = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds"


def pobierz_mecze() -> list[dict]:
    klucz_api = os.getenv("ODDS_API_KEY")

    if not klucz_api:
        raise RuntimeError("Brak ODDS_API_KEY w pliku .env")

    parametry = {
        "apiKey": klucz_api,
        "regions": "eu",
        "bookmakers": "betclic_fr",
        "markets": "h2h",
        "oddsFormat": "decimal",
        "dateFormat": "iso",
    }

    odpowiedz = httpx.get(
        ADRES_API,
        params=parametry,
        timeout=20,
    )

    odpowiedz.raise_for_status()

    print(
        "Pozostałe kredyty:",
        odpowiedz.headers.get("x-requests-remaining"),
    )

    wynik = []

    for wydarzenie in odpowiedz.json():
        bukmacher = next(
            iter(wydarzenie.get("bookmakers", [])),
            None,
        )

        if bukmacher is None:
            continue

        rynek = next(
            (
                element
                for element in bukmacher.get("markets", [])
                if element["key"] == "h2h"
            ),
            None,
        )

        if rynek is None:
            continue

        gospodarz = wydarzenie["home_team"]
        goscie = wydarzenie["away_team"]

        kursy = {
            rezultat["name"]: rezultat["price"]
            for rezultat in rynek["outcomes"]
        }

        kurs_1 = kursy.get(gospodarz)
        kurs_x = kursy.get("Draw")
        kurs_2 = kursy.get(goscie)

        if None in (kurs_1, kurs_x, kurs_2):
            continue

        wynik.append(
            {
                "zewnetrzne_id": wydarzenie["id"],
                "data_rozpoczecia": wydarzenie["commence_time"],
                "gospodarz": gospodarz,
                "goscie": goscie,
                "kurs_1": kurs_1,
                "kurs_x": kurs_x,
                "kurs_2": kurs_2,
                "bukmacher": bukmacher["title"],
            }
        )

    return wynik


if __name__ == "__main__":
    mecze = pobierz_mecze()

    print(f"Pobrano meczów: {len(mecze)}")

    for mecz in mecze:
        print()
        print(f'{mecz["gospodarz"]} - {mecz["goscie"]}')
        print(f'Data: {mecz["data_rozpoczecia"]}')
        print(
            f'1: {mecz["kurs_1"]} | '
            f'X: {mecz["kurs_x"]} | '
            f'2: {mecz["kurs_2"]}'
        )