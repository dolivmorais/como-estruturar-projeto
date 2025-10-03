from pipeline.extract import extract_from_excel
from pipeline.transform import constact_data_frames
from pipeline.load import save_to_excel 


def main():
    data_frame_list = extract_from_excel("data/input")
    data_frame = constact_data_frames(data_frame_list)
    save_to_excel(data_frame, "data/output", "output")

    print("Processo concluido com sucesso!")


if __name__ == "__main__":
    main()