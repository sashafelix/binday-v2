package app.routers;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.Instant;
import java.util.HashMap;
import java.util.Map;

import app.schemas.HealthResponse;

@RestController
@RequestMapping("/api/v1")
public class HealthController {

    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> getHealth() {
        String version = System.getenv("APP_VERSION");
        if (version == null) {
            version = "unknown";
        }
        String timestamp = Instant.now().toString();

        HealthResponse data = new HealthResponse(version, timestamp);

        Map<String, Object> envelope = new HashMap<>();
        envelope.put("data", data);
        envelope.put("success", true);
        envelope.put("timestamp", timestamp);

        return ResponseEntity.ok(envelope);
    }
}