"""
Snapshot de estado para Design by Contract.

Responsabilidade:
- Registrar estados ANTES e DEPOIS da execução de funções contratadas
- NÃO validar
- NÃO lançar exceções
- NÃO conhecer domínio

Uso:
Chamado exclusivamente pelos decorators de contrato.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, UTC
from typing import Any, Dict, List, Optional


# =========================
# Estrutura do Snapshot
# =========================

@dataclass(frozen=True)
class Snapshot:
    timestamp: str
    function_name: str
    state_before: Dict[str, Any]
    state_after: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None


# =========================
# Storage em memória
# =========================

_SNAPSHOTS: List[Snapshot] = []


# =========================
# API pública do módulo
# =========================

def record_snapshot(
    *,
    function_name: str,
    state_before: Dict[str, Any],
    state_after: Dict[str, Any],
    metadata: Optional[Dict[str, Any]] = None
) -> None:
    """
    Registra um snapshot de estado.
    """
    snapshot = Snapshot(
        timestamp=datetime.now(UTC).isoformat(),
        function_name=function_name,
        state_before=state_before,
        state_after=state_after,
        metadata=metadata,
    )

    _SNAPSHOTS.append(snapshot)


def get_snapshots() -> List[Snapshot]:
    """
    Retorna todos os snapshots registrados.
    """
    return list(_SNAPSHOTS)


def clear_snapshots() -> None:
    """
    Limpa os snapshots (útil para testes).
    """
    _SNAPSHOTS.clear()


def export_snapshots_as_dict() -> List[Dict[str, Any]]:
    """
    Exporta snapshots em formato serializável (dict),
    ideal para enviar a outra IA ou salvar em JSON futuramente.
    """
    return [asdict(s) for s in _SNAPSHOTS]