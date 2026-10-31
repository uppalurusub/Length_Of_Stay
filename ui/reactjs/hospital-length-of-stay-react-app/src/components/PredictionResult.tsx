import {
  Alert,
  Box,
  Card,
  CardContent,
  Chip,
  Divider,
  Grid,
  Stack,
  Typography,
} from "@mui/material";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CalendarMonthIcon from "@mui/icons-material/CalendarMonth";
import MedicalServicesIcon from "@mui/icons-material/MedicalServices";
import AccessTimeIcon from "@mui/icons-material/AccessTime";

interface Props {
  response: any;
}

import "../styles/PredictionResult.css";

const formatDate = (date: string) =>
  new Date(date).toLocaleString();

export default function PredictionResult({ response }: Props) {
  if (!response) return null;

  return (
    <Card className="prediction-card">

      <CardContent>

        <Typography variant="h4" gutterBottom>
          Prediction Result
        </Typography>

        <Alert
          severity="success"
          icon={<CheckCircleIcon />}
          sx={{ mb: 4 }}
        >
          {response.message}
        </Alert>

        <Grid container spacing={3}>

          <Grid size={{ xs: 12, md: 4 }}>
            <Card className="metric-card los-card">
              <CardContent>

                <Typography className="metric-title">
                  Predicted LOS
                </Typography>

                <Typography className="los-value">
                  {response.predicted_length_of_stay_days}
                </Typography>

                <Typography className="metric-unit">
                  Days
                </Typography>

              </CardContent>
            </Card>
          </Grid>

          <Grid size={{ xs: 12, md: 4 }}>
            <Card className="metric-card">
              <CardContent>

                <Stack spacing={3}>

                  <Box className="metric-row">
                    <MedicalServicesIcon color="primary" />

                    <Box>
                      <Typography className="label">
                        Model
                      </Typography>

                      <Chip
                        label={response.model_name}
                        color="primary"
                      />
                    </Box>
                  </Box>

                  <Divider />

                  <Box className="metric-row">
                    <CalendarMonthIcon color="primary" />

                    <Box>
                      <Typography className="label">
                        Prediction Time
                      </Typography>

                      <Typography>
                        {formatDate(response.prediction_timestamp)}
                      </Typography>
                    </Box>
                  </Box>

                  <Divider />

                  <Box className="metric-row">
                    <AccessTimeIcon color="primary" />

                    <Box>
                      <Typography className="label">
                        Status
                      </Typography>

                      <Chip
                        color="success"
                        label="Prediction Successful"
                      />
                    </Box>
                  </Box>

                </Stack>

              </CardContent>
            </Card>
          </Grid>

        </Grid>

      </CardContent>

    </Card>
  );
}