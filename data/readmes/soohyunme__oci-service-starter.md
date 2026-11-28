# OCI Service Starter

> AI 에이전트와 함께 OCI에 소규모 웹 서비스 실행 환경을 구축하기 위한 Terraform 스타터

OCI Service Starter는 Oracle Cloud Infrastructure(OCI)에 서비스를 처음 배포하려는 1인 개발자와 소규모 팀을 위한 저장소입니다. 저장소를 Clone한 뒤 제공된 요청문을 AI 에이전트에 전달하면, 에이전트가 필요한 설정을 확인하고 Terraform Plan을 설명한 후 사용자의 승인을 받아 환경을 구축합니다.

OCI Console의 여러 설정 화면을 직접 따라가는 대신, 검토 가능한 Terraform 코드와 에이전트 가이드를 사용합니다. Terraform 적용 전에는 생성되는 리소스, 외부에 공개되는 포트와 과금 가능성을 반드시 확인합니다.

> [!WARNING]
> Terraform을 적용하면 실제 OCI 리소스가 생성됩니다. 계정 유형, 리전, 기존 사용량과 현재 가격 정책에 따라 비용이 발생할 수 있습니다. 이 저장소는 무료 사용을 보장하지 않습니다.

이 구성은 기존 Compute에 연결하거나 기존 리소스를 가져오지 않습니다. 별도의 VCN, Compute와 Boot Volume을 새로 생성합니다.

별도 설정이 없으면 Root Compartment에 새 환경을 만듭니다. 기존 전용 Compartment를 사용하고 싶을 때만 에이전트에 알려주면 됩니다. 이 저장소는 Compartment 자체를 만들거나 기존 OCI 리소스를 변경하지 않습니다.

## 구축되는 환경

- VCN, Public Subnet, Internet Gateway와 Security List
- Compute 교체 후에도 다시 연결할 수 있는 Reserved Public IPv4
- 단일 `VM.Standard.A1.Flex` Compute 인스턴스
- 기본 사양: 2 OCPU, 12GB Memory, 100GB Boot Volume
- Docker Engine과 Docker Compose
- 웹 요청 전달과 HTTPS 인증서 관리를 위한 Caddy
- Password와 Root 로그인을 비활성화한 SSH Key 인증

초기 구축 직후에는 Reserved Public IP의 HTTP 상태 확인만 제공합니다. 도메인을 연결하면 Caddy가 HTTPS 인증서 발급과 요청 전달을 담당합니다.

상세한 OCI 리소스와 실행 구조는 [전체 아키텍처](docs/assets/architecture.png)와 [구성 설명](docs/architecture.md)에서 확인할 수 있습니다.

## 준비 사항

- OCI Account
- OCI에 등록한 API Signing Key와 OCI 설정 파일(`~/.oci/config`)
- SSH Key Pair
- Terraform 1.10 이상
- 터미널과 로컬 파일을 사용할 수 있는 AI 에이전트

API Signing Key 생성과 등록은 [Oracle 공식 문서](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm)를 참고합니다. 준비가 완료되지 않았더라도 구축 요청문을 전달하면 에이전트가 누락된 필수 항목을 안내합니다. API Private Key와 SSH Private Key는 이 저장소에 복사하지 않습니다.

## 시작하기

### 1. 저장소 Clone

```bash
git clone https://github.com/soohyunme/oci-service-starter.git
cd oci-service-starter
```

### 2. 에이전트에 구축 요청

Clone한 디렉터리를 AI 에이전트에서 열고 다음 요청을 전달합니다.

```text
이 저장소의 AGENTS.md와 prompts/provision-oci.md를 읽고 OCI 서비스 환경 구축을 준비해 주세요.

확인할 수 없는 정보만 질문하고, Terraform Plan에서 생성·변경되는 리소스와 과금 가능성을 이해하기 쉽게 설명해 주세요. 제 명시적 승인 전에는 terraform apply를 실행하지 마세요.
```

전용 Compartment는 선택 사항입니다. 사용하려면 요청문 끝에 `기존 전용 Compartment를 사용합니다: <Compartment OCID>` 한 줄만 추가합니다. 그 외에는 별도로 지정하지 않아도 됩니다.

에이전트는 자동으로 확인할 수 없는 필수 정보만 요청하고 `terraform/terraform.tfvars` 작성을 돕습니다. 이후 Terraform Plan을 바탕으로 다음 내용을 설명합니다.

- 생성·변경·교체·삭제되는 OCI 리소스
- 선택한 OCI Profile, Region과 배포 범위(Root 또는 전용 Compartment)
- Compute 사양과 Boot Volume 크기
- 외부에 공개되는 포트와 SSH 접근 범위
- 서비스 중단 또는 데이터 손실 가능성
- 확인 가능한 과금 항목과 검증하지 못한 전제

### 3. Plan 검토 후 적용 승인

Plan과 설명을 확인한 뒤에만 에이전트에 적용을 승인합니다. 에이전트는 승인된 변경을 적용하고 다음 상태를 검증합니다.

- Compute 인스턴스 실행 상태
- Cloud-Init 완료 여부
- Docker와 Caddy 실행 상태
- Reserved Public IP의 HTTP 상태 확인 응답
- SSH Key 기반 관리 접속

적용 후 생성되는 로컬 Terraform State와 입력 파일은 이후 변경과 삭제에 필요합니다. Clone한 디렉터리의 `terraform/terraform.tfstate`와 `terraform/terraform.tfvars`를 안전하게 보존하고 Git에 추가하지 않습니다.

자세한 준비, 검토와 삭제 절차는 [시작 가이드](docs/getting-started.md)를 참고합니다.

## 애플리케이션 연결

기본 환경 구축이 끝나면 기존 Docker 이미지 또는 애플리케이션 저장소를 연결할 수 있습니다. 다음 요청문을 에이전트에 전달합니다.

> 기본 Compute는 ARM64 기반입니다. 애플리케이션 이미지는 `linux/arm64` 또는 Multi-Architecture를 지원해야 합니다.

```text
이 저장소의 AGENTS.md와 prompts/connect-application.md를 읽고 현재 OCI 환경에 제 애플리케이션을 연결할 준비를 해 주세요.

기존 이미지와 Registry 구성을 우선 확인하고, 변경 계획과 Secret 처리 방식을 설명한 뒤 제 승인을 받아 적용해 주세요.

애플리케이션 위치: <로컬 저장소 경로 또는 컨테이너 이미지>
```

에이전트는 Dockerfile, 이미지 Registry, 애플리케이션 포트, 도메인, 환경변수와 CPU Architecture 호환성을 확인합니다. 기존 GHCR, OCIR 또는 호환 Registry가 있으면 해당 구성을 우선 사용합니다.

구체적인 절차는 [애플리케이션 연결 가이드](docs/connect-application.md)에서 확인할 수 있습니다.

## 환경 삭제

더 이상 환경이 필요하지 않으면 동일한 Clone 디렉터리에서 다음 요청을 에이전트에 전달합니다.

```text
이 저장소의 AGENTS.md와 docs/getting-started.md의 환경 삭제 절차를 읽고 삭제를 준비해 주세요.

Terraform 삭제 계획으로 삭제될 리소스와 사라지는 데이터를 먼저 설명하고, 제 명시적 승인 전에는 terraform destroy를 실행하지 마세요. 삭제 후 OCI에 남은 리소스와 Terraform 밖에서 별도로 정리해야 할 항목도 알려 주세요.
```

Compute의 Boot Volume과 그 안의 애플리케이션 데이터도 삭제됩니다. 필요한 데이터는 승인 전에 별도로 백업합니다.

## 안전 기준

- `terraform apply`와 `terraform destroy`는 사용자의 명시적 승인 후에만 실행합니다.
- OCI API Key, Auth Token, SSH Private Key, Terraform State와 애플리케이션 Secret을 Git이나 에이전트 응답에 노출하지 않습니다.
- SSH는 Key 인증만 허용하며 기본 웹 진입점 외의 애플리케이션 포트는 외부에 공개하지 않습니다.
- 기존 OCI 리소스를 자동으로 가져오거나 변경하지 않습니다.
- 리소스 교체, 삭제, 중단과 데이터 손실 가능성은 일반 변경과 구분해 설명합니다.

SSH 접속 위치까지 제한하려면 [고급 SSH 보안 설정](docs/advanced-ssh-security.md)을 적용할 수 있습니다.

## 지원 범위

첫 버전은 한 대의 OCI Compute에서 하나 이상의 소규모 컨테이너 서비스를 운영하는 시작점을 제공합니다. 다음 항목은 포함하지 않습니다.

- Kubernetes, k3s와 Argo CD
- OCI Load Balancer와 다중 인스턴스 고가용성
- 애플리케이션별 CI/CD 자동 생성
- Database, Backup과 통합 Observability 구성
- Free Tier 적용 여부 자동 판정

자세한 기준은 [저장소 범위](docs/project-scope.md)를 참고합니다.

## 문서

- [시작 가이드](docs/getting-started.md)
- [애플리케이션 연결 가이드](docs/connect-application.md)
- [아키텍처 설명](docs/architecture.md)
- [고급 SSH 보안 설정](docs/advanced-ssh-security.md)
- [저장소 범위](docs/project-scope.md)

## 라이선스

이 저장소는 [MIT License](LICENSE)로 제공됩니다.
