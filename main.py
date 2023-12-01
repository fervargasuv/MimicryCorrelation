import MimicryFacade

def main():
    fachada = MimicryFacade.MimicryFacade()
    matriz_x = fachada.process_data([
        "./Mimicry_Catalogue/EoM_C1_VC1-Catalogue.csv",
        "./Mimicry_Catalogue/EoM_C2_VC1-Catalogue.csv",
        "./Mimicry_Catalogue/EoM_C3_VC1-Catalogue.csv",
        "./Mimicry_Catalogue/EoM_C4_VC1-Catalogue.csv",
        "./Mimicry_Catalogue/EoM_C5_VC1-Catalogue.csv",
        "./Mimicry_Catalogue/EoM_C6_VC1-Catalogue.csv"
    ])


if __name__ == "__main__":
    main()