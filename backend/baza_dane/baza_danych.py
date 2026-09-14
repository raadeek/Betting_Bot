import sqlite3
from datetime import datetime, timezone
from pathlib import Path

PLIK_BAZY = Path(__file__).resolve().parent / "betsim.db"


def utworz_tabele() -> None:
    polaczenie = sqlite3.connect(PLIK_BAZY)

    try:
        polaczenie.execute(
            """
            CREATE TABLE IF NOT EXISTS matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                external_id TEXT NOT NULL,
                season TEXT NOT NULL,
                matchweek INTEGER,
                home_team TEXT NOT NULL,
                away_team TEXT NOT NULL,
                commence_time TEXT NOT NULL,
                home_odds REAL NOT NULL,
                draw_odds REAL NOT NULL,
                away_odds REAL NOT NULL,
                bookmaker TEXT NOT NULL,
                odds_updated_at TEXT NOT NULL,
                UNIQUE(source, external_id)
            )
            """
        )

        polaczenie.commit()
    finally:
        polaczenie.close()


def zapisz_mecze(mecze: list[dict]) -> None:
    polaczenie = sqlite3.connect(PLIK_BAZY)
    czas_aktualizacji = datetime.now(timezone.utc).isoformat()

    try:
        for mecz in mecze:
            polaczenie.execute(
                """
                INSERT INTO matches (
                    source,
                    external_id,
                    season,
                    matchweek,
                    home_team,
                    away_team,
                    commence_time,
                    home_odds,
                    draw_odds,
                    away_odds,
                    bookmaker,
                    odds_updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(source, external_id)
                DO UPDATE SET
                    season = excluded.season,
                    matchweek = COALESCE(
                        excluded.matchweek,
                        matches.matchweek
                    ),
                    home_team = excluded.home_team,
                    away_team = excluded.away_team,
                    commence_time = excluded.commence_time,
                    home_odds = excluded.home_odds,
                    draw_odds = excluded.draw_odds,
                    away_odds = excluded.away_odds,
                    bookmaker = excluded.bookmaker,
                    odds_updated_at = excluded.odds_updated_at
                """,
                (
                    "the_odds_api",
                    mecz["zewnetrzne_id"],
                    "2026/27",
                    None,
                    mecz["gospodarz"],
                    mecz["goscie"],
                    mecz["data_rozpoczecia"],
                    mecz["kurs_1"],
                    mecz["kurs_x"],
                    mecz["kurs_2"],
                    mecz["bukmacher"],
                    czas_aktualizacji,
                ),
            )

        polaczenie.commit()
    finally:
        polaczenie.close()


def pobierz_zapisane_mecze() -> list[dict]:
    polaczenie = sqlite3.connect(PLIK_BAZY)
    polaczenie.row_factory = sqlite3.Row

    try:
        wiersze = polaczenie.execute(
            """
            SELECT *
            FROM matches
            ORDER BY commence_time
            """
        ).fetchall()

        return [dict(wiersz) for wiersz in wiersze]
    finally:
        polaczenie.close()