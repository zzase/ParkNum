# ParkNum
it help you When you park your car. (Used Yolo, Ocr etc...)

사용법 

#설정
1. google vision api 계정 생성, json파일 다운 -> 환경변수 설정 : cmd에서 setx GOOGLE_APPLICATION_CREDENTIALS (json 파일 위치)(json 파일 이름).json

2.darkflow : pip install tensorflow==1.14.0, pip install opencv-python(4.2.0.32), pip install cython (0.29.15) pip install darkflow

3.firebase : pip install firebase_admin, pip install pirebase
*pirebase install중 setup.py 오류시 https://m.blog.naver.com/vvv1ct0r/220930787642 참고하여 수정 

4.darkflow\darkflow\net\yolo\misc.py 수정
 parkingLabel = ["parknum"] 추가
 park_models =['parking-yolo-obj'] 추가
 
 def labels(meta,FLAGS) 수정 
 def labels(meta, FLAGS):
model = os.path.basename(meta['name']) 
if model in voc_models: print("Model has a VOC model name, loading VOC labels.") meta['labels'] = labels20 
else: file = FLAGS.labels 
if model in coco_models: print("Model has a coco model name, loading coco labels.") file = os.path.join(FLAGS.config, coco_names) elif model == 'yolo9000': print("Model has name yolo9000, loading yolo9000 labels.") file = os.path.join(FLAGS.config,nine_names) elif model in park_models: print("Model has a park model name, loading park labels.") file =os.path.join(FLAGS.config,park_names) with open(file, 'r') as f: meta['labels'] = list() labs = [l.strip() for l in f.readlines()] for lab in labs: if lab == '----': break meta['labels'] += [lab] if len(meta['labels']) == 0: meta['labels'] = labels20 else: meta['labels'] = parkingLabel

#참고링크 
google api : https://ssungkang.tistory.com/m/entry/Google-Vision-API-%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%9C-%EA%B8%80%EC%9E%90-%EC%9D%B8%EC%8B%9D

darkflow : https://junyoung-jamong.github.io/deep/learning/2019/01/22/Darkflow%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%B4-YOLO%EB%AA%A8%EB%8D%B8-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%94%94%ED%85%8D%EC%85%98-%EA%B5%AC%ED%98%84-in-windows.html

firebase : https://romeoh.tistory.com/entry/Firebase-Python-Firebase-Realtime-Database
