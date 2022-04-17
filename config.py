"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", None) or "19217751"
        self.API_HASH: str = os.environ.get("API_HASH", None) or "65031483c1e0a9d18b1f3f54bb4114d8"
        self.SESSION: str = os.environ.get("PYROGRAM_SESSION", None) or "BQBi1hARdGbSNhAvd3pjHQsyASgPtiHlxyQkh9noX2dGwTrugzFCbHhDT8ADnSpG73dUuOZ5SOtK8TAiDinpPq5FU9N9g5aLgWL2AvpRTX2Q4GEJhuh9BhkJB2uL4_Sz_MuVXe-n9DJNiN1DucO_nhYCaSj0Vd-YhhFq8nxqRjvc-Gf0F_XIwNPMo6ICKg4AHJF3Rpmx4ZrSn9fxl5kMW-9PIfK9smWbBy3G-CFUSA4AVwmrkBGVVi-2xT7u4EEr2aPzZR9ebqr-H82VPIdi5XRSKYiJ8yCjmCCfuXzTWzKoLh_3f5sM0qHTB6a94CKML_Sv_GJJL0CscQJEFCWPIzwvAAAAATg_3UsA"
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5238676811").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.CUSTOM_QUALITY: str = os.environ.get("CUSTOM_QUALITY", "high").lower()


config = Config()
