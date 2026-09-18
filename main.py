from app.repositories import TariffRepository, ServiceRepository

tariff_repo = TariffRepository()
service_repo = ServiceRepository()

print("=== Тарифы ===")
tariffs = tariff_repo.get_all()
for t in tariffs:
    print(t)

print("\n=== Услуги ===")
services = service_repo.get_all()
for s in services:
    print(s)