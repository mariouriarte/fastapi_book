from fastapi import FastAPI, Depends, APIRouter

# This will cause depfunc() to be called for all path functions under router.
router = APIRouter(..., dependencies=[Depends(depfunc)])
