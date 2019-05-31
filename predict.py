import argparse
import json
from allennlp.predictors import Predictor
from allennlp.models.archival import load_archive
import drop_library
from tqdm import tqdm
import os

if __name__ == "__main__":
    # Parse arguments

    parser = argparse.ArgumentParser()
    parser.add_argument("--archive_file", type = str, required = True,
                        help = "URL for a trained model file")
    parser.add_argument("--input_file", type=str, required=True,
                        help='path for drop input files')
    parser.add_argument("--output_file", type=str, required=True,
                        help="path for predictions output file")
    args = parser.parse_args()

    # Create predictor
    archive = load_archive(args.archive_file)
    predictor = Predictor.from_archive(archive, "naqanet")
    
    predictions = {}

    count = 0
    # Run on input file & collect answers
    input_json = json.load(open(args.input_file, encoding = "utf8"))
    passages = input_json.items()
    for passage_id , passage_data in tqdm(passages):
        if (count > 1):
            break;
        count += 1
        passage = passage_data["passage"]
        for qa_pair in passage_data["qa_pairs"]:
            question = qa_pair["question"]
            query_id = qa_pair["query_id"]
            prediction = predictor.predict(question = question, passage = passage)
            answer = prediction["answer"]
            answer_type = answer["answer_type"]
            ans_str = str(answer["value"]) \
                      if (answer_type != "count")  \
                         else str(answer["count"])
            predictions[query_id] = ans_str

    # Write output file
    os.makedirs(os.path.dirname(args.output_file))
    with open(args.output_file, "w", encoding = "utf8") as fout:
        json.dump(predictions, fout, indent=4)
