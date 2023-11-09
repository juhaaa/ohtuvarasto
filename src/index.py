from varasto import Varasto


def main():
    mehua = Varasto(100.0)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
