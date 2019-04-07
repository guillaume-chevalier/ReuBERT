import json
import os


def extract_question_from_squad():
    training_data = []
    with open(os.path.join(__file__, 'dev-v2.0.json'), encoding='utf-8') as json_file:
        data = json.load(json_file)
        for elem in data['data']:
            result = {}
            result['text'] = extract_text_from_paragraph(elem['paragraphs'])
            result['qa'] = extract_questions_from_paragraph(elem['paragraphs'])
            training_data.append(result)

    with open(os.path.join(__file__, 'squad_questions_beautified.json'), 'w', encoding='utf-8') as outfile:
        json.dump(training_data, outfile)


def extract_text_from_paragraph(para):
    text = []
    for elem in para:
        text.append(elem["context"] + ' ')
    return text


def extract_questions_from_paragraph(para):
    result = []
    for elem in para:
        section = {}
        section["subtext"] = elem["context"]
        section["qas"] = []
        for qa in elem['qas']:
            qa_elem = {}
            qa_elem["question"] = qa["question"] + ''
            qa_elem["answers"] = []
            for ans in qa["answers"]:
                qa_elem["answers"].append(ans['text'])
            section["qas"].append(qa_elem)
        result.append(section)
    return result

if __name__ == '__main__':
    extract_question_from_squad()
