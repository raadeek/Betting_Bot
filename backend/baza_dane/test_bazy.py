from baza_danych import pobierz_zapisane_mecze


mecze = pobierz_zapisane_mecze()

print(f"Liczba meczów: {len(mecze)}")

for mecz in mecze:
    print(
        f'{mecz["id"]}: '
        f'{mecz["home_team"]} - {mecz["away_team"]} | '
        f'1: {mecz["home_odds"]} | '
        f'X: {mecz["draw_odds"]} | '
        f'2: {mecz["away_odds"]}'
    )