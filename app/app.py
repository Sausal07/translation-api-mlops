from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
import logging

# from transliteration_load_ct_multi import transliteration_model_ct_multi,pass_variable_ct,initModeltransliteration
from translate_load_multi import translation_model_multi,pass_variable,initModeltranslation
from translate_load_il_2_il import translation_model_ILIL

app = FastAPI(
    title="Translation API",
    version="1.0.0"
)



@app.on_event("startup")
async def load_model_before_server_starts():
    # initModeltransliteration()
    initModeltranslation()

# # Your serializer equivalent
# class transliterationRequest(BaseModel):
#     # input_text: str = Field(..., alias='ip_text')
#     ip_text: str
#     srcLang: str
#     tgtLang: str
#     nSuggestions: Optional[int] = 1

class translationRequest(BaseModel):
    # input_text: str = Field(..., alias='ip_text')
    ip_text: str
    srcLang: str
    tgtLang: str
    delimiter: str
    nSuggestions: Optional[int] = 1

# Dummy implementations (replace with actual ones)
# def pass_variable_ct(ip):
#     logging.info(f"Client IP: {ip}")

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/version")
def version():
    return {
        "service": "translation-api",
        "version": "1.0.0"
    }

# def transliteration_model_ct_multi(input_text, srcLang, tgtLang, nOptions):
#     if srcLang not in ['en', 'hi'] or tgtLang not in ['hi', 'en']:
#         return "Currently this web service is not supporting"
#     return [f"{input_text}-{srcLang}-{tgtLang}-{i+1}" for i in range(nOptions)]


# @app.post("/getTransliteration")
# async def generic_transliteration(request: Request):
#     try:
#         body = await request.json()
#         print("Incoming request body:", body)
        
#         # # Remap 'ip_text' to 'input_text' if needed
#         # if 'ip_text' in body:
#         #     body['input_text'] = body.pop('ip_text')
        
#         # Validate input
#         input_data = transliterationRequest(**body)
#         input_text = input_data.ip_text
#         srcLang = input_data.srcLang.lower()
#         tgtLang = input_data.tgtLang.lower()
#         nOptions = input_data.nSuggestions

#         # Extract IP
#         ip = request.headers.get("x-forwarded-for")
#         if ip:
#             ip = ip.split(",")[0]
#         else:
#             ip = request.client.host

#         print("=" * 80)
#         print(ip)
#         pass_variable_ct(ip)

#         # Process
#         op = transliteration_model_ct_multi(input_text, srcLang, tgtLang, nOptions)

#         if op == 'Currently this web service is not supporting':
#             raise HTTPException(status_code=401, detail="Invalid Input language pairs")

#         return JSONResponse(content={"Output": op})

#     except Exception as e:
#         return JSONResponse(content={"error": str(e)}, status_code=400)



@app.post("/getTranslation")
async def generic_translation(request: Request):
    try:
        body = await request.json()
        print("Incoming request body:", body)
        
        # # Remap 'ip_text' to 'input_text' if needed
        # if 'ip_text' in body:
        #     body['input_text'] = body.pop('ip_text')
        
        # Validate input
        input_data = translationRequest(**body)
        ip_text = input_data.ip_text
        srcLang = input_data.srcLang.lower()
        tgtLang = input_data.tgtLang.lower()
        delimiter = input_data.delimiter
        nSuggestions = input_data.nSuggestions

        # Extract IP
        ip = request.headers.get("x-forwarded-for")
        if ip:
            ip = ip.split(",")[0]
        else:
            ip = request.client.host

        print("=" * 80)
        print(ip)
        pass_variable(ip)

        # # Process
        # op = transliteration_model_ct_multi(input_text, srcLang, tgtLang, nOptions)

        # if op == 'Currently this web service is not supporting':
        #     raise HTTPException(status_code=401, detail="Invalid Input language pairs")

        # return JSONResponse(content={"Output": op})

        if srcLang == 'eng-latn' or tgtLang == 'eng-latn':
            # print('ip_text view:',ip_text)  
            op = translation_model_multi(ip_text.strip(),srcLang,tgtLang,delimiter,nSuggestions)
            # print('op view:',op)
        else:
            op = translation_model_ILIL(ip_text.strip(),srcLang,tgtLang,delimiter,nSuggestions)
      
        if op =='Currently this web service is not supporting':
            return JsonResponse({"error": "Invalid Input language pairs"}, status=401)

        else:
            # response={"Output": op}
            # print(response)
            return JSONResponse(content={"Output": op})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)



#uvicorn app:app --host 0.0.0.0 --port 8000