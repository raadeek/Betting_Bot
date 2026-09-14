from baza_danych import (
    pobierz_zapisane_mecze,
    utworz_tabele,
    zapisz_mecze,
)
from pobieranie_meczy import pobierz_mecze


def main() -> None:
    utworz_tabele()

    mecze_z_api = pobierz_mecze()
    zapisz_mecze(mecze_z_api)

    zapisane_mecze = pobierz_zapisane_mecze()

    print(f"Mecze zapisane w bazie: {len(zapisane_mecze)}")

    for mecz in zapisane_mecze:
        print()
        print(f'{mecz["home_team"]} - {mecz["away_team"]}')
        print(f'Data: {mecz["commence_time"]}')
        print(f'Kolejka: {mecz["matchweek"]}')
        print(
            f'1: {mecz["home_odds"]} | '
            f'X: {mecz["draw_odds"]} | '
            f'2: {mecz["away_odds"]}'
        )


if __name__ == "__main__":
    main()