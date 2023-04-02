import os
import datetime
import psutil
from pydantic import BaseModel


class ProcessMemoryScheme(BaseModel):
    rss: int
    vms: int
    shared: int
    text: int
    lib: int
    data: int
    dirty: int
    uss: int
    pss: int
    verification_date: str


class FullMemoryScheme(BaseModel):
    total: int
    available: int
    percent: float
    used: int
    free: int
    active: int
    inactive: int
    buffers: int
    cached: int
    shared: int
    slab: int
    verification_date: str


class MemoryMonitoring:
    @staticmethod
    def get_process_memory_info() -> ProcessMemoryScheme:
        process = psutil.Process(os.getpid())
        memory_info = process.memory_full_info()
        return ProcessMemoryScheme(
            rss=memory_info.rss,
            vms=memory_info.vms,
            shared=memory_info.shared,
            text=memory_info.text,
            lib=memory_info.lib,
            data=memory_info.data,
            dirty=memory_info.dirty,
            uss=memory_info.uss,
            pss=memory_info.pss,
            verification_date=str(datetime.datetime.now()),
        )

    @staticmethod
    def get_full_memory_info() -> FullMemoryScheme:
        memory_info = psutil.virtual_memory()
        return FullMemoryScheme(
            total=memory_info.total,
            available=memory_info.available,
            percent=memory_info.percent,
            used=memory_info.used,
            free=memory_info.free,
            active=memory_info.active,
            inactive=memory_info.inactive,
            buffers=memory_info.buffers,
            cached=memory_info.cached,
            shared=memory_info.shared,
            slab=memory_info.slab,
            verification_date=str(datetime.datetime.now()),
        )
