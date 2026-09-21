from app.repositories import ServiceRepository, TariffRepository


def main() -> None:
    tariff_repo = TariffRepository()
    service_repo = ServiceRepository()

    print("=== Тарифы ===")
    for tariff in tariff_repo.get_all():
        print(f"{tariff.id}: {tariff.name} — {tariff.price} ₽")

    print("\n=== Услуги ===")
    for service in service_repo.get_all():
        print(f"{service.id}: {service.name} — {service.price} ₽")


if __name__ == "__main__":
    main()
